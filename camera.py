#Hes(Home entertainment system)
import cv2
import sys
from easygui import *
import numpy as np
from PIL import Image
import face_recognition
import PIL.ImageOps

x = 0

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
else:
        rval = False
while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
        	break;
        y = str(x)
        
        
vc.release()
cv2.destroyWindow("preview")

