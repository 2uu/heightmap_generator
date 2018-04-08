import cv2
import numpy as np
import sys
import random


args = sys.argv

range = 30

rows = 1025#img.shape[0]
cols = 1025#img.shape[1]

img= np.zeros((rows, cols, 1), np.uint8)

for x in xrange(0,rows) :
    for y in xrange(0,cols) :

        img[x,y] = random.uniform(255-range,255)

cv2.imshow('image',img)

keycode = cv2.waitKey(0)
if keycode == ord('s'):
    cv2.imwrite("heightmap.png", img)
