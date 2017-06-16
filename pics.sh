#!/bin/bash
# This is used to collect images from a live web cam
# Any live webcam can be used ass long it is public and you know the url
for i in `seq 1 300`; do
wget http://livecam-static.olemiss.edu/union.jpg
sleep 10
done
