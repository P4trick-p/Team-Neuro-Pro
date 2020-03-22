import numpy as np
import glob
import imageio
import time # for debugging

def signaltonoise(a, axis=0, ddof=0): # deprecated scipy function
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)
# Tworzenie tablicy 2D z artystami i ich obrazami
rows, cols = (3, 50)
arr = [[0]*cols]*rows
#art = ( glob.glob("base_original\Beksinski\\*.jpg") , glob.glob("base_original\Hockney\\*.jpg") , glob.glob("base_original\Gogh\\*.jpg"))
art = ( glob.glob("base_original\Beksinski\\*.jpg") , glob.glob("base_original\Hockney\\*.jpg") , glob.glob("base_original\Gogh\\*.jpg"))

for x in range(rows):
    i = 0
    for image_path in art[x]:           # Coś tu nie gra
        im = imageio.imread(image_path)
        arr[x][i] = im
        i += 1
    x += 1
x=0
i=0
# Liczenie SNR (Signal to Noise Ratio) // Jednostka?
avg = [0]*cols
SNR = [[0]*cols]*rows
for x in range(rows):
    for i in range(cols):
        img = arr[x][i]
        SNR[x][i] = signaltonoise(img , axis=None )
        print(i+1, 'SNR =' , SNR[x][i])
        i += 1
    snr = SNR[x]
    avg[x] = np.average(snr)
    print('Average SNR = ' , avg[x])
    time.sleep(2)
    x += 1
