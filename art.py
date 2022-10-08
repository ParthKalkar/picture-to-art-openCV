# imports
import cv2
import numpy as np

# reading image
image = cv2.imread('nature.jpg')

# resize image - using cubic interpolation
image_resize = cv2.resize(image, None, fx=1, fy=1)

# removing impurity
image_cleared = cv2.medianBlur(image_resize, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)

image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s = 5)

# bilateralFilter
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

for _ in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for _ in range(3):
    image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

# sharpening image
gaussian_mask = cv2.GaussianBlur(image_filtered, (7,7), 2)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

# display image
cv2.imshow('original', image)
cv2.imshow("Image", image_resize)
cv2.imshow("Image Sharp", image_sharp)
cv2.waitKey(0)

cv2.destroyAllWindows()
