import cv2
import numpy as np
import sys
from PIL import Image
img = cv2.imread(sys.argv[1], -1)

# extract red channel
red_channel = img[:,:,2]

#save image
cv2.imwrite('final2.png',red_channel) 

img = Image.open('final2.png')
pixels = img.load()

for i in range(img.size[0]): # for every pixel:
	for j in range(img.size[1]):
		if pixels[i,j] >= 150:                  
			pixels[i,j] = 150
		else:
		     pixels[i,j] = 0

for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
                if pixels[i,j] >= 140:                  
                        pixels[i,j] = 255 
                else:
                        pixels[i,j] = 0

img.save('final.png')

