from os import wait
import serial
import numpy as np
import time

import matplotlib.pyplot as plt

from scipy.ndimage.filters import gaussian_filter
import seaborn as sns
 
ser = serial.Serial('/dev/cu.usbmodem141101',9600,timeout=None)

plt.subplots(figsize=(8, 4))


while True:
    line = ser.readline()
    line = line.decode("utf-8")[:-2].split(",")

    temp = line[0]
    pixels = line[1:-1]

    pixels = np.reshape(pixels,[8, 8]).astype(np.float32)

    # seaborn用のコード　超解像ができないので没
    # line_array_smooth = gaussian_filter(line_array, sigma=1)
    # sns.heatmap(line_array_smooth, vmin=20, cmap ="inferno" , cbar=True)

    plt.subplot(1, 1, 1)
    fig = plt.imshow(pixels, cmap="inferno", interpolation="bicubic", vmin= 26)
    plt.colorbar()

    while ser.inWaiting() == 0:
        time.sleep(0.01)

    plt.pause(.01)
    plt.clf()


ser.close()