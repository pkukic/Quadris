from PIL import Image, ImageOps
from pixelmatch.contrib.PIL import pixelmatch
from sqlib import run_select, select_duplicates


def flip(image):
    return ImageOps.flip(image)

def mirror(image):
    return ImageOps.mirror(image)

def rotate_1(image):
    return image.rotate(90, expand=True)

def rotate_2(image):
    return image.rotate(180, expand=True)

def rotate_3(image):
    return image.rotate(270, expand=True)

def rotate_4(image):
    return image

def delta_1(image):
    return rotate_1(mirror(image))

def delta_2(image):
    return rotate_1(flip(image))



if __name__ == '__main__':

    resp = run_select('../unique/polyminoes.db', select_duplicates())
    transforms = [flip, mirror, rotate_1, rotate_2, rotate_3, rotate_4, delta_1, delta_2]

    for img1, img2 in resp['table']:
        img1, img2 = list(map(lambda x: (x[:-4] + '.png').replace("r_color", "plot").replace("colors", "plots"), [img1, img2]))
        fnames = (img1, img2)
        img1, img2 = list(map(lambda x: Image.open(x), [img1, img2]))
        for t in transforms:
            print(fnames, pixelmatch(img1, t(img2)))
            if pixelmatch(img1, t(img2)) < 1000:
                print("WOAH")


    ### Sanity check ###
    # img1 = "../unique/plots/plot_16a.png"
    # img2 = "../unique/plots/plot_16b.png"
    # print(pixelmatch(Image.open(img1), Image.open(img2)))