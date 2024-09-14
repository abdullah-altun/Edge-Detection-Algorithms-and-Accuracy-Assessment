import cv2
import numpy as np
import json
import matplotlib.pyplot as plt

from proccesing import *

# with open("images/labels/_annotations.cocoEdge.json") as f:
#     data = json.load(f)
# segmentation_data = data["annotations"][0]["segmentation"][0]
image_total = cv2.imread(r"images/subpixelEedges/Image_20240914112340424.bmp")
# h,w,_ = image.shape
# image_total = np.full((h,w,_),255,dtype=np.uint8)
# segmentation_points = np.array(segmentation_data).reshape((-1, 1, 2)).astype(np.int32)
# cv2.polylines(image_total, [segmentation_points], isClosed=True, color=(0, 0, 0), thickness=3)

image_total[image_total < 221] = 0
image_total[image_total > 220] = 255

edgeImage = image_total.copy()

edgeImage[image_total == 0] = 255
edgeImage[image_total == 255] = 0

closed_image = edgeImage
closed_image[(closed_image[:, :, 0] == 255) & (closed_image[:, :, 1] == 255) & (closed_image[:, :, 2] == 255)] = [0, 0, 255]
closed_image = cv2.cvtColor(closed_image, cv2.COLOR_BGR2BGRA)
closed_image[np.all(closed_image[:, :, :3] == [0, 0, 0], axis=-1)] = [0, 0, 0, 0]
cv2.imwrite("edgeDetect.png",closed_image)

with open("images/labels/2_annotations.coco.json") as f:
    data = json.load(f)
segmentation_data = data["annotations"][0]["segmentation"][0]
image = cv2.imread(r"images/calibCamera/2Image_20240914100238765.bmp")
h,w,_ = image.shape
image_total = np.full((h,w,_),255,dtype=np.uint8)
segmentation_points = np.array(segmentation_data).reshape((-1, 1, 2)).astype(np.int32)
cv2.polylines(image_total, [segmentation_points], isClosed=True, color=(0, 0, 0), thickness=3)
cv2.imwrite("Image.png",image_total)
imageMask = processing("Image.png")
cv2.imwrite("ImageMask.png",imageMask)

mask = cv2.imread('ImageMask.png', cv2.IMREAD_GRAYSCALE)
mask_normalized = mask / 255
result = image * mask_normalized[:, :, np.newaxis]
cv2.imwrite("Image.png",result.astype(np.uint8))

original_img = cv2.imread('Image.png')
overlay_img = cv2.imread('edgeDetect.png', cv2.IMREAD_UNCHANGED)  # Saydam görüntü
h, w = original_img.shape[:2]
overlay_img = cv2.resize(overlay_img, (w, h))
red_mask = (overlay_img[:, :, 0] == 0) & (overlay_img[:, :, 1] == 0) & (overlay_img[:, :, 2] == 255)
black_mask = (original_img[:, :, 0] == 0) & (original_img[:, :, 1] == 0) & (original_img[:, :, 2] == 0)
result_img = original_img.copy()
result_img[red_mask & black_mask] = [255, 0, 0] 
result_img[red_mask & ~black_mask] = [0, 0, 255]  

cv2.imwrite("ImageMerge.jpg",result_img)

result_img = result_img[300:-1000,500:-1200]
blue_mask = (result_img[:, :, 0] == 255) & (result_img[:, :, 1] == 0) & (result_img[:, :, 2] == 0)

rows, cols = blue_mask.shape
max_streak = 0
max_streak_coords = (0, 0, 0) 

for row in range(rows):
    streak = 0
    start_col = 0
    for col in range(cols):
        if blue_mask[row, col]:
            if streak == 0:
                start_col = col
            streak += 1
            if streak > max_streak:
                max_streak = streak
                max_streak_coords = (row, start_col, col)
        else:
            streak = 0

# En uzun seriyi yeşil yap
print(max_streak_coords)
if max_streak > 0:
    row, start_col, end_col = max_streak_coords
    result_img[row, start_col:end_col+1] = [0, 255, 0]  # Yeşil renk

# Sonucu kaydet
cv2.imwrite('result_image.png', result_img)

print(f'En uzun mavi piksel serisi {max_streak} piksel uzunluğunda ve {(1000/8.3)*max_streak} mikron hata bulunuyor')