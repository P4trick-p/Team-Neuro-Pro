from matplotlib import pyplot as plt
import numpy as np
import imageio
import time
import glob
import cv2
import matplotlib.image as mpimg

artists = ('Beksiński','Hockney','van Gogh')
arts = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg") )

X = 0
axs = [0] * 3
axm = [0] * 3
color = ('b','g','r')
for X in range(3):
    fig, axs[X] = plt.subplots(5, 10)
    fig, axm[X] = plt.subplots(5, 10)

for X in range(3):
    i = 0
    images = [0] * 50
    hist = [0] * 50
    for image_path in arts[X]:
        im = imageio.imread(image_path) #Wczytywanie obrazów z katalogu
        images[i] = im
        i += 1
    xx = 0
    I = 0
    for xx in range(5):
        x = 0
        for x in range(10):
            i = 0
            for i, col in enumerate(color):
                axm[X][xx, x].imshow(images[I])
                # imgplot = plt.imshow(img)
            I += 1

    i=0
    I = 0
    xx = 0
    for xx in range(5):
        x = 0
        for x in range(10):
            i=0
            for i,col in enumerate(color):
                hist[I] = cv2.calcHist([images[I]],[i],None,[256],[0,256])
                axs[X][xx, x].plot(hist[I],color = col)
                plt.xlim([0,256])
            I += 1
plt.show()
