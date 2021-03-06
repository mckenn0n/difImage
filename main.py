import numpy as math
import matplotlib.pyplot as plot
import os
import sys
from PIL import Image

args = sys.argv
upper_lim = int(args[2]) - 1

if len(args) != 3:
	print("Wrong number of Command Line arguments.")
	sys.exit()

averageImage =0.0
differenceImage=0.0
for i in range(int(args[2])):
	image = Image.open("images/starbucks.jpg")
	if i > 0:
		image =Image.open("images/starbucks.jpg."+str(i))
	image = math.float32(image)
	averageImage += image
for i in range(0,upper_lim):
	if i == 0:
		image1 = Image.open("images/starbucks.jpg")
		image2 =Image.open("images/starbucks.jpg."+str(i+1))
		image1= math.float32(image1)
		image2 = math.float32(image2)
		difference = math.absolute(image1-image2)
		differenceImage+=difference
	else:
		image1 = Image.open("images/starbucks.jpg."+str(i))
		image2 =Image.open("images/starbucks.jpg."+str(i+1))
		image1= math.float32(image1)
		image2 = math.float32(image2)
		difference = math.absolute(image1-image2)
		differenceImage+=difference
averageImage=averageImage/int(args[2])
differenceImage=differenceImage/upper_lim
for row in range(len(differenceImage)):
	for col in range(len(differenceImage[row])):
		diff = differenceImage[row, col]
		avg = averageImage[row, col]
		new = math.mean(diff)/math .mean(avg)
		if new > float(args[1]):
			averageImage[row][col] = [255,0,0]
differenceImage =differenceImage.clip(0,255)
averageImage =averageImage.clip(0,255)
averageImage=math.uint8(averageImage)
differenceImage=math.uint8(differenceImage)
plot.imshow(averageImage)
plot.show()
