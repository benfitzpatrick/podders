import cv
import sys
if(len(sys.argv) > 1):
    capture = cv.CaptureFromCAM(1)
    img = cv.QueryFrame(capture)
    cv.SaveImage(sys.argv[1], img)