import numpy as np
import matplotlib.image as mpimg


def rgb2gray(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])


if __name__ == '__main__':
    for i in range(100):
        img = mpimg.imread(f'input/{i}.jpg')
        gray = rgb2gray(img)
        mpimg.imsave(f'output/{i}.jpg', gray, cmap='gray')
