import search_solutions
import numpy as np
import pickle
import os

from sqlib import select_greater_than, sum_of_indices, run_sqlite

def rotations_and_reflections(image):
    ro1 = np.rot90(image, 1)
    ro2 = np.rot90(image, 2)
    ro3 = np.rot90(image, 3)
    ro4 = np.rot90(image, 4)
    mu1 = np.fliplr(image)
    mu2 = np.flipud(image)
    delta1 = np.rot90(np.fliplr(image), 3)
    delta2 = np.rot90(np.fliplr(image), 1)
    return ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2

def dicts_from_image(image):
    return [search_solutions.label_to_dict(l) for l in rotations_and_reflections(image)]

def check_subsetability(d_parent, d_child):
    v = [d_child[k].issubset(d_parent[k]) for k in range(1, 6+1)]
    v = np.array(v)
    return np.all(v == 1)

def load_parents(image):
    transforms = rotations_and_reflections(image)
    sums = list(map(sum_of_indices, transforms))
    ind_list = []
    d_parents = []
    for s in sums:
        select = run_sqlite('../unique/polyminoes.db', select_greater_than(s))
        fnames = [item[0] for item in select['table']]
        indices = [int(item.split("_")[-1].split(".")[0]) for item in fnames]
        ind_list.extend(indices)
    ind_list = list(set(ind_list))
    for i in ind_list:
        fname = f'../unique/pickled_dicts/dict_{i}.pickle'
        print('Loaded ' + fname)
        with open(fname, 'rb') as handle:
            d_parents.append(pickle.load(handle))
    return ind_list, d_parents

def reverse_image(i, k):
    fname = f'../unique/labels/r_label_{i}.mat'
    label = search_solutions.load_label(fname)
    if k <= 3:
        return np.rot90(label, 3 - k)
    if k == 4:
        return np.fliplr(label)
    if k == 5:
        return np.flipud(label)
    if k == 6:
        return np.rot90(np.fliplr(label), 3)
    else:
        return np.rot90(np.fliplr(label), 1)

def find_parent(image):
    color_image = [[] for i in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[i])):
            color_image[i].append(search_solutions.get_color_from_label(image[i][j]))
        
    d_children = dicts_from_image(image)
    parents_indices, d_parents = load_parents(color_image)
    for i in range(len(d_parents)):
        d_parent = d_parents[i]
        for k in range(len(d_children)):
            if check_subsetability(d_parent, d_children[k]):
                return reverse_image(parents_indices[i], k)
    return None