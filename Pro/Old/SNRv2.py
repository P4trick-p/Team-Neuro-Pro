import numpy as np
import glob
import imageio
import time # for debugging

#### Debugger ####
#print()
#time.sleep()
##################

def signaltonoise(a, axis=0, ddof=0): # deprecated scipy function
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)
# Tworzenie tablicy 2D z artystami i ich obrazami
rows, cols = (3, 50)
arr = [[0]*cols]*rows
art = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg") )
arty = ('Beksinski','Hockney','Gogh')
for x in range(rows):
    i=0
    #print(arty[x])
    for image_path in art[x]:# Coś tu nie gra
        #print(image_path)
        arr[x][i] = imageio.imread(image_path)

# Liczenie SNR (Signal to Noise Ratio) //
avg = [0]*cols
SNR = [[0]*cols]*rows

x = 0
for x in range(rows):
    i = 0
    for i in range(cols):
        img = arr[x][i]
        #print(img)
        #time.sleep(100)
        SNR[x][i] = signaltonoise(img)
        print(i+1, 'SNR =' , SNR[x][i])

    snr = SNR[x]
    avg[x] = np.mean(snr)
    print('Average SNR = ' , avg[x])
print(SNR[2][49])
time.sleep(100)