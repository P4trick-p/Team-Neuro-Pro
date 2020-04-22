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
df = [0]*50
i=0
for image_path in arts[1]:
    im = imageio.imread(image_path)  # Wczytywanie obrazów z katalogu
    img[i] = im
    i += 1

for x in range(50):
    for i,col in enumerate(color):
        his[x] = cv2.calcHist([img[x]],[i],None,[256],[0,256])

        #plt.plot(his[x],color = col)
        #plt.xlim([0,256])
    df[x] = pd.DataFrame(his[x])


df_merged = pd.concat([df[1],df[2],df[3],df[4],df[5],df[6],df[7],df[8],df[9],df[10],df[11],df[12],df[13],df[14],df[15],df[16],df[17],df[18],df[19],df[20],df[21],df[22],df[23],df[24],df[25],df[26],df[27],df[28],df[29],df[30],df[31],df[32],df[33],df[34],df[35],df[36],df[37],df[38],df[39],df[40],df[41],df[42],df[43],df[44],df[45],df[46],df[47],df[48],df[49],df[50]], ignore_index=True)
# Get the frequencies of the combined histogram
hist, bins = np.histogram(df_merged)
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





