import os
import cv2
pathOut = r"C:/Users/Me/Out/"
count = 0
counter = 1
listing = os.listdir(r'./cookieMonster/framePrack')  #change directory
for vid in listing:
    vid = r"./cookieMonster/framesFromPrack" #change directory
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    while success:
        success,image = cap.read()
        print('read a new frame:',success)
        if count%30 == 0 :
             cv2.imwrite(pathOut + 'frame%d.jpg'%count,image)
        count+=1
