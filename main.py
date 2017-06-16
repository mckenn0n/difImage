import numpy as math
import matplotlib.pyplot as plot
import os
import sys
from PIL import Image

args = sys.argv

if len(args) != 2:
	print("Wrong number of Command Line arguments.")
	sys.exit()

averageImage =0.0
differenceImage=0.0
for i in range(300):
	image = Image.open("union.jpg")
	if i > 0:
		image =Image.open("union.jpg."+str(i))
	image = math.float32(image)
	averageImage += image
for i in range(0,299):
	if i == 0:
		image1 = Image.open("union.jpg")
		image2 =Image.open("union.jpg."+str(i+1))
		image1= math.float32(image1)
		image2 = math.float32(image2)
		difference = math.absolute(image1-image2)
		differenceImage+=difference
	else:
		image1 = Image.open("union.jpg."+str(i))
		image2 =Image.open("union.jpg."+str(i+1))
		image1= math.float32(image1)
		image2 = math.float32(image2)
		difference = math.absolute(image1-image2)
		differenceImage+=difference
averageImage=averageImage/300
differenceImage=differenceImage/299
for row in range(len(differenceImage)):
	for col in range(len(differenceImage[row])):
		diff = differenceImage[row, col]
		avg = averageImage[row, col]
		new = math.mean(diff)/math .mean(avg)
		#avg= differenceImage[row][col][0]
		#avg+=differenceImage[row][col][1]
		#avg+=differenceImage[row][col][2]
		#avg2= averageImage[row][col][0]
		#avg2+=averageImage[row][col][1]
		#avg2+=averageImage[row][col][2]
		#new = (avg)/(avg2)
		if new > float(args[1]):
			averageImage[row][col] = [255,0,0]
differenceImage =differenceImage.clip(0,255)
averageImage =averageImage.clip(0,255)
averageImage=math.uint8(averageImage)
differenceImage=math.uint8(differenceImage)
plot.imshow(averageImage)
plot.show()
