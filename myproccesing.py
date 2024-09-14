import cv2
import numpy as np


"""image_total= cv2.imread("images/dexined/BIPED2CLASSIC/fused/Image_20240913165513423_caliResult1.png")

print(np.unique(image_total))

# image[:1000,:] = 255
# image

image_total[image_total < 221] = 0
image_total[image_total > 220] = 255

edgeImage = image_total.copy()

edgeImage[image_total == 0] = 255
edgeImage[image_total == 255] = 0

closed_image = edgeImage
closed_image[(closed_image[:, :, 0] == 255) & (closed_image[:, :, 1] == 255) & (closed_image[:, :, 2] == 255)] = [0, 0, 255]
closed_image = cv2.cvtColor(closed_image, cv2.COLOR_BGR2BGRA)
closed_image[np.all(closed_image[:, :, :3] == [0, 0, 0], axis=-1)] = [0, 0, 0, 0]
cv2.imwrite("edgeDetect2.png",closed_image)"""

image = cv2.imread("ImageMerge.jpg")

cv2.imwrite("zden.jpg",image[300:-1000,:])