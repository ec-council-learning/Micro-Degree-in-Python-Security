import numpy as np
import matplotlib.image as mpimg
import multiprocessing


def rgb2gray(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])

def read_and_save(i):
    img = mpimg.imread(f'input/{i}.jpg')
    gray = rgb2gray(img)
    mpimg.imsave(f'output/{i}.jpg', gray, cmap='gray')


if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        pool.map(read_and_save, [i for i in range(100)])
