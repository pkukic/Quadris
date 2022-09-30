import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import sys

import search_solutions
import disp_solutions

from matplotlib.widgets import Button

color_to_rgb = {
    0: 'white',
    1: 'blue', # monomino
    2: 'aqua', # I
    3: 'green', # L
    4: 'yellow', # square
    5: 'orange', # T
    6: 'red', # Z
}

n_polyminoes = {
    0: 1,
    1: 1,
    2: 2,
    3: 5,
    4: 5,
    5: 4,
    6: 4,
}

n_squares = {
    0: 1,
    1: 1,
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
}

index_color_quantity = {k: (color_to_rgb[k], n_polyminoes[k]) for k in color_to_rgb.keys()}

print(index_color_quantity)

cmap_list = []
for k in index_color_quantity.keys():
    cmap_list += [index_color_quantity[k][0]]*index_color_quantity[k][1]

print(cmap_list)

# Label #i will correspond to the correct color
cmap = colors.ListedColormap(cmap_list)

color_to_label = {
    0: [0],
    1: [1],
    2: [2, 3],
    3: [4, 5, 6, 7, 8],
    4: [9, 10, 11, 12, 13],
    5: [14, 15, 16, 17],
    6: [18, 19, 20, 21],
}

original_color_to_label = {
    0: [0],
    1: [1],
    2: [2, 3],
    3: [4, 5, 6, 7, 8],
    4: [9, 10, 11, 12, 13],
    5: [14, 15, 16, 17],
    6: [18, 19, 20, 21],
}

COLOR = 0
LABEL = 0
N = 0

def get_label_and_update(i):
    global LABEL, N, COLOR, color_to_label
    N = n_squares[COLOR]
    if len(color_to_label[i]) == 0:
        color_to_label[i] = []
        return LABEL
    else:
        val = color_to_label[i][0]
        if len(color_to_label[i]) > 1:
            color_to_label[i] = color_to_label[i][1:]
        else:
            color_to_label[i] = []
        return val



if __name__ == '__main__':    
    image = np.zeros((9, 9))
    fig, ax = plt.subplots()
    cax = ax.pcolormesh(image, cmap=cmap, vmin=-1, vmax=22, edgecolors='k', linewidth=2)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xticks(np.arange(9+1))
    ax.set_yticks(np.arange(9+1))

    clear_ax = plt.axes([0.05, 0.8, 0.1, 0.1])
    mono_ax = plt.axes([0.05, 0.7, 0.1, 0.1])
    I_ax = plt.axes([0.05, 0.6, 0.1, 0.1])
    L_ax = plt.axes([0.05, 0.5, 0.1, 0.1])
    Square_ax = plt.axes([0.05, 0.4, 0.1, 0.1])
    T_ax = plt.axes([0.05, 0.3, 0.1, 0.1])
    Z_ax = plt.axes([0.05, 0.2, 0.1, 0.1])

    axes_arr = [clear_ax, mono_ax, I_ax, L_ax, Square_ax, T_ax, Z_ax]
    colors_arr = list(range(7))
    labels_arr = [color_to_label[k] for k in colors_arr]

    def set_val_on_click(event):
        global COLOR, LABEL, N, color_to_label, original_color_to_label, image
        for i in range(7):
            if event.inaxes == axes_arr[i]:
                if i != 0:    
                    print(i)
                    print(color_to_label)
                    COLOR = i
                    LABEL = get_label_and_update(COLOR)
                    N = n_squares[COLOR]
                    print(f"Color set to {COLOR}, label set to {LABEL}, N set to {N}")
                else:
                    image = np.zeros((9, 9))
                    COLOR = 0
                    LABEL = 0
                    N = 0
                    color_to_label = original_color_to_label
                    cax.set_array(image.ravel())
                    fig.canvas.draw()

    clear_button = Button(clear_ax, 'Clear')
    monomino_button = Button(mono_ax, 'Mono')
    I_button = Button(I_ax, 'I tetro')
    L_button = Button(L_ax, 'L tetro')
    Square_button = Button(Square_ax, 'S tetro')
    T_button = Button(T_ax, 'T tetro')
    Z_button = Button(Z_ax, 'Z tetro')

    buttons_arr = [clear_button, monomino_button, I_button, L_button, Square_button, T_button, Z_button]
    for button in buttons_arr:
        button.on_clicked(set_val_on_click)

    def onclick(event):
        
        global LABEL, N, color_to_label
        print('clicked')

        # Check if *this* button was clicked
        if event.inaxes == ax:
            
            if N == 0:
                print(color_to_label)
                new_label = get_label_and_update(search_solutions.get_color_from_label(LABEL))
            
                if new_label != LABEL:
                    LABEL = new_label
            
                else:
                    raise ValueError("All polyminoes of this kind already used up!")
            
                print(f"LABEL set to {LABEL}")

            N -= 1
            fx = int(np.floor(event.xdata))
            fy = int(np.floor(event.ydata))
            print(N, fy, fx)

            # Update the image
            image[fy, fx] = LABEL

            # Unravel it so you can draw the canvas
            cax.set_array(image.ravel())
            fig.canvas.draw()
    
    fig.canvas.mpl_connect('button_press_event', onclick)
    
    # Find the solution of the board on Ctrl + S
    def press(event):
        global image
        sys.stdout.flush()
        if event.key == 'ctrl+s':
            print(image)
            image = disp_solutions.find_parent(image)
            cax.set_array(image.ravel())
            fig.canvas.draw()
    
    # Remove the default Ctrl + S and replace it with our custom functionality
    plt.rcParams['keymap.save'].remove('ctrl+s')
    fig.canvas.mpl_connect('key_press_event', press)
    plt.show()
