import cv2     # for capturing videos
import math   # for mathematical operations
# import matplotlib.pyplot as plt    # for plotting the images
# import pandas as pd
# from keras.preprocessing import image   # for preprocessing the images
# import numpy as np    # for mathematical operations
# from keras.utils import np_utils
# from skimage.transform import resize   # for resizing images
import sys
from glob import glob

vid_directory = sys.argv[1]
vids = glob(vid_directory + '*.mp4')

#to allow for unique file names
filenum = 0 + sys.argv[2]

for videoFile in vids:
	count = 0
	cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
	frameRate = cap.get(5) #frame rate
	x=1
	while(cap.isOpened()):
	    frameId = cap.get(1) #current frame number
	    ret, frame = cap.read()
	    if (ret != True):
	        break
	    if (frameId % math.floor(frameRate) == 0):
	        filename =f"./Data/UnsortedVid/file{filenum}frame{count}.jpg"
	        count+=1
	        cv2.imwrite(filename, frame)
	        print("write ", filename)
	cap.release()
	print ("Done!")
	filenum += 1