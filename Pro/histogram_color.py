from matplotlib import pyplot as plt
import numpy as np
import cv2

file = '01.jpg'
img = cv2.imread(file)
color = ('b','g','r')
plt.figure()
for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()

