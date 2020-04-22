from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import glob
import imageio
import time

arts = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg") )



img = [0] * 50
color = ('b','g','r')
plt.figure()
his = [0]*50
df = [[0]*3]*50

for I in range(3):
    i = 0
    for image_path in arts[I]:
        im = imageio.imread(image_path)  # Wczytywanie obrazów z katalogu
        img[i] = im
        i += 1

    for x in range(50):


        for i,col in enumerate(color):
            his[x] = cv2.calcHist([img[x]],[i],None,[256],[0,256])

            plt.plot(his[x],color = col)
            plt.xlim([0,256])
        df[x] = pd.DataFrame(his[x])

df_merged = [0]*3
I= 0
hist = [0]*3
bins = [0]*3
for I in range(3):
    df_merged[I] = pd.concat([df[I]], ignore_index=True)
    # Get the frequencies of the combined histogram
    hist[I], bins[I] = np.histogram(df_merged[I])
    # Normalize by 4
    hist_norm = hist / 4.0
    width = 0.9 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2

    # plot the Un-normalited frequencies
    plt.bar(center, hist, align='center', width=width)
    plt.title('Non- Normalized Histogram')
    plt.show()

    # plot the normalized frequencies
    plt.bar(center, hist_norm, align='center', width=width)
    plt.title('Normalized Histogram')
    plt.show()





