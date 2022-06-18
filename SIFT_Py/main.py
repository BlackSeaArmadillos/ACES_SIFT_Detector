import cv2
import numpy as np
import sift

sigma = 1.6
num_intervals = 3
assumed_blur=0.5
image_border_width=5


image = cv2.imread('box.png')

cv2.imshow('Box', image)
cv2.waitKey(0)

image = sift.generateBaseImage(image, sigma, assumed_blur)

cv2.imshow('Box', image)
cv2.waitKey(0)