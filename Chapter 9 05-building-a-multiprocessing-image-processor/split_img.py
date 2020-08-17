import matplotlib.image as mpimg


if __name__ == '__main__':
    img = mpimg.imread('input/ship.jpg')
    for i in range(100):
        mpimg.imsave(f'input/{i}.jpg', img)
