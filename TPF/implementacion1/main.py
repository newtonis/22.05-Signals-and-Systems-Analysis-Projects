import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


img = cv2.imread('imagen1.jpeg', 3)

img_intensity = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


print(img_intensity)

plt.imshow(img_intensity, cmap="gray")

sobelx = cv2.Sobel(img_intensity, cv2.CV_64F, 1, 0, ksize=9)
sobely = cv2.Sobel(img_intensity, cv2.CV_64F, 0, 1, ksize=9)

#print(img)

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#plt.imshow(sobelx, cmap="gray")



plt.show()





