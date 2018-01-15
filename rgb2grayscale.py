###################################
# Convert an rgb image to grayscale
# and filter to eliminate the background
# Date 14/01/2018
# author: Valerio Mazzone
##################################

import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
import matplotlib.cm as cm

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

file = 'prova.jpg'
image = misc.imread(file)

grey = np.zeros((image.shape[0], image.shape[1])) # init 2D numpy array
# get row number
for rownum in range(len(image)):
   for colnum in range(len(image[rownum])):
      grey[rownum][colnum] = weightedAverage(image[rownum][colnum])


for rownum in range(len(image)):
   for colnum in range(len(image[rownum])):
      if grey[rownum][colnum] < 90:
          grey[rownum][colnum] = 0

plt.imshow(grey, cmap = cm.Greys_r)
plt.show()
