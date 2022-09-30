import scipy.io as sio
import numpy as np
import pickle
import os

label_to_color = {
    # All elements have to be tuples,
    # So force tuples here: type((0,)) == <type 'tuple'> and type((0)) = <type 'int'>
    (0,): 0,
    (1,): 1,
    (2, 3): 2,
    (4, 5, 6, 7, 8): 3,
    (9, 10, 11, 12, 13): 4,
    (14, 15, 16, 17): 5,
    (18, 19, 20, 21): 6,
}

color_to_label = {
    1: [1],
    2: [2, 3],
    3: [4, 5, 6, 7, 8],
    4: [9, 10, 11, 12, 13],
    5: [14, 15, 16, 17],
    6: [18, 19, 20, 21],
}

def get_color_from_label(l):
    for key, value in label_to_color.items():
        if l in key:
            return value
    return None


def load_label(fname):
    return sio.loadmat(fname)['r_label']


def load_everything(a, b):
    fnames_labels = [f"../unique/labels/r_label_{i}" for i in range(a, b+1)]
    loaded_labels = [load_label(f) for f in fnames_labels]
    return loaded_labels


def label_to_dict(label):
    d = {
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
    }
    
    for i in range(1, 21+1):
        
        indices = np.argwhere(label == i)
        
        if indices.size != 0:

            # This has to be sorted because otherwise you couldn't compare 
            # partial solutions with full solutions properly
            indices = tuple(tuple(item) for item in indices)
            indices = tuple(sorted(indices, key=lambda x: x[0]+x[1]))
            color = get_color_from_label(i)

            # Add the sorted tuple to the set
            d[color].add(indices)
    
    return d

def labels_to_dicts(labels):
    return [label_to_dict(l) for l in labels]


def make_pickles(a, b):
    labels = load_everything(a, b)
    dicts = labels_to_dicts(labels)
    for i in range(a,b+1):
        fname = f'../unique/pickled_dicts/dict_{i}.pickle'
        print('Pickled ' + fname)
        with open(fname, 'wb') as handle:
            pickle.dump(dicts[i - 1], handle, protocol=pickle.HIGHEST_PROTOCOL)
        

if __name__ == '__main__':
    make_pickles(1, len(os.listdir('../unique/labels/')))
