# difImage

### Requires:
* numpy
* matplotlib
* PIL

### Run shell script:

    ./pics.sh https://livecam-static.olemiss.edu/starbucks.jpg

### Run python code:

    python3 main.py .4 300

### pics.sh

The pics.sh can be ran with any webcam linked to the internet that uses still images. Save the link to the image file of the webcam and pics.sh with the link instead of https://livecam-static.olemiss.edu/starbucks.jpg.

This script will download 300 images and save them to the image directory.

### main.py

Highlight areas of change in a set of images.

main.py takes two command line arguments. The first being the diffence threshold that you want highlighted. 0 highlights any change 1 highlights very little change. The input can range from 0 to 1 a floats. The second is the number of images you want to find the differance in.
