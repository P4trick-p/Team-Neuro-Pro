from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import imageio
import glob
import time
import math
import cv2

artists = ('Beksiński','Hockney','van Gogh', 'Modigliani')
arts = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg"), glob.glob("base\Modigliani\\*.jpg") )
avg = np.zeros((4,3))
avg_rgb = np.zeros(600)
avg_rgb.shape = (4, 50, 3)
avg_dis = np.zeros(400)
avg_dis.shape = (4, 50, 2)
avg_diss = np.zeros(600)
avg_diss.shape = (4, 3, 50)
dis = np.zeros(200)
dis.shape = (4,50)

dates0 = np.array([1967.5,1968.5,1969.3,1969.6,1969.9,1970.2,1970.4,1970.6,1970.8,1971.5,1972.4,1972.8,1973.3,
                   1973.6,1973.9,1974.5,1975.4,1975.8,1976.2,1976.4,1976.6,1976.8,1976.9,1977.3,1977.6,1977.9,
                   1978.1,1978.3,1978.5,1978.7,1979.1,1979.3,1979.5,1979.7,1980.1,1980.3,1980.5,1981.1,1981.3,
                   1981.5,1981.7,1981.9,1982.1,1982.3,1982.5,1982.7,1983.1,1983.3,1983.5,1984.5])
dates1 = np.array([1937.1,1937.2,1964.1,1966.1,1966.2,1967.1,1967.2,1967.3,1967.4,1968.1,1968.2,1971.1,1972.1,
                   1972.2,1973.1,1974.1,1979.1,1988.1,1988.2,1989.1,1990.1,1990.2,1991.1,1992.1,1993.1,1995.1,
                   1995.2,1996.1,1996.2,1997.1,1997.2,1998.1,1998.2,2000.1,2000.2,2000.3,2002.1,2005.1,2005.2,
                   2007.1,2008.1,2008.2,2009.1,2009.2,2014.1,2014.2,2015.1,2015.2,2017.1,2017.2])
avg_diss[0,2] = dates0
avg_diss[1,2] = dates1
#avg_diss[2,2] = dates2
#avg_diss[3,2] = dates3
color = ('b','g','r')
hist = [0] * 50

def getAverageRGBN(image):
  # Given PIL Image, return average value of color as (r, g, b)
  im = np.array(image) # get image as numpy array
  w,h,d = im.shape # get shape
  im.shape = (w*h, d) # change shape
  return np.array(np.average(im, axis=0)) # get average

X = 0
axm = [0] * 4
axs = [0] * 4

for X in range(4):
    fig, axs[X] = plt.subplots(5, 10)
    fig, axm[X] = plt.subplots(5, 10)

for X in range(4):
    i = 0
    images = [0] * 50
    his = [0] * 50
    for image_path in arts[X]:
        images[i] = imageio.imread(image_path) #Wczytywanie obrazów z katalogu
        avg_rgb[X, i] = getAverageRGBN(images[i])
        i += 1

    xx = 0
    I = 0
    for xx in range(5):
        x = 0
        for x in range(10):
            i = 0
            for i, col in enumerate(color):
                axm[X][xx, x].imshow(images[I])

            I += 1

    if X < 2:
        #3D SCATTER PLOT
        x = 0
        for x in range(50):
            if avg_rgb[X,x,0] < avg_rgb[X,x,1] and avg_rgb[X,x,0] < avg_rgb[X,x,2]:
                avg_dis[X, x, 0] = abs(avg_rgb[X, x, 1] - avg_rgb[X, x, 0])
                avg_dis[X, x, 1] = abs(avg_rgb[X, x, 2] - avg_rgb[X, x, 0])
            if avg_rgb[X, x, 1] < avg_rgb[X, x, 0] and avg_rgb[X, x, 1] < avg_rgb[X, x, 2]:
                avg_dis[X, x, 0] = abs(avg_rgb[X, x, 0] - avg_rgb[X, x, 1])
                avg_dis[X, x, 1] = abs(avg_rgb[X, x, 2] - avg_rgb[X, x, 1])
            else:
                avg_dis[X, x, 0] = abs(avg_rgb[X, x, 0] - avg_rgb[X, x, 2])
                avg_dis[X, x, 1] = abs(avg_rgb[X, x, 1] - avg_rgb[X, x, 2])
            avg_diss[X, 0, x] = avg_dis[X, x, 0]
            avg_diss[X, 1, x] = avg_dis[X, x, 1]

            dis[X, x] = math.sqrt((avg_diss[X, 0, x]**2)+(avg_diss[X, 1, x]**2))

        fig = plt.figure()
        ax = Axes3D(fig)

        sequence_containing_x_vals = list(avg_diss[X,0])
        sequence_containing_y_vals = list(avg_diss[X,1])
        sequence_containing_z_vals = list(avg_diss[X,2])

        ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
        font = 12
        ax.set_xlabel('$A$', fontsize=font)
        ax.set_ylabel('$B$', fontsize=font)
        ax.set_zlabel('$Data$', fontsize=font)

    #HISTOGRAMS
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
    avg[X] = np.average(avg_rgb[X], axis=0)
    print(artists[X])
    print(avg[X])
    i=0

print(avg_rgb)
plt.show()
#np.savetxt("rgb.csv", avg_rgb[0], delimiter=";")
