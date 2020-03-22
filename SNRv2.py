import numpy as np
import glob
import imageio
# for debugging
import time

# deprecated scipy function
def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

# Tworzenie wektora z obrazami

#art = [0]*3
#img = [0]*50
rows, cols = (3, 50)
arr = [[0]*cols]*rows

# 1 - Beksinski, 2 - Gogh, 3 - Hockney
B = glob.glob("im_base_original\Beksinski\\*.jpg")
G = glob.glob("im_base_original\Gogh\\*.jpg")
H = glob.glob("im_base_original\Hockney\\*.jpg")
artists = [ B , G , H]
for x in range(rows):
    i = 0
    for image_path in artists[x]:
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
    snr = SNR[x]
    avg[x] = np.average(snr)
    print('Average SNR = ' , avg)
    time.sleep(5)