import numpy as np
import glob
import imageio

# deprecated scipy function
def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

# Tworzenie wektora z obrazami
img = [0] * 50
i = 0
for image_path in glob.glob("im_base_original\Gogh\\*.jpg"):
    im = imageio.imread(image_path)
    img[i] = im
    i += 1

# Liczenie SNR (Signal to Noise Ratio) // Jednostka?
snr = [0] * 50
for x in range(50):
    snr[x] = signaltonoise(img[x] , axis=None )
    print(x+1, 'SNR =' , snr[x])