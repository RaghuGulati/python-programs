import cv2
import numpy as np
import sys
from PIL import Image
img = cv2.imread(sys.argv[1], -1)

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
#    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

#result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

# extract red channel
red_channel = result_norm[:,:,2]

#save image
cv2.imwrite('final.png',red_channel) 

img = Image.open('final.png')
pixels = img.load()

for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
                if pixels[i,j] >= 160:                  
                        pixels[i,j] = 150

for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
                if pixels[i,j] >= 140:                  
                        pixels[i,j] = 255 
                else:
                        pixels[i,j] = 0

img.save('final.png')

