import cv2.cv as cv
import os
from datetime import datetime
import time

class MotionDetectorInstantaneous():
    
    def onChange(self, val): #callback when the user change the detection threshold
        self.threshold = val
    
    def __init__(self,threshold=17, showWindows=False):
        self.writer = None
        self.font = None
        self.show = showWindows #Either or not show the 2 windows
        self.frame = None
    
        self.capture=cv.CaptureFromCAM(0)
        self.frame = cv.QueryFrame(self.capture) #Take a frame to init recorder
        
        self.frame1gray = cv.CreateMat(self.frame.height, self.frame.width, cv.CV_8U) #Gray frame at t-1
        cv.CvtColor(self.frame, self.frame1gray, cv.CV_RGB2GRAY)
        
        #Will hold the thresholded result
        self.res = cv.CreateMat(self.frame.height, self.frame.width, cv.CV_8U)
        
        self.frame2gray = cv.CreateMat(self.frame.height, self.frame.width, cv.CV_8U) #Gray frame at t
        
        self.width = self.frame.width
        self.height = self.frame.height
        self.nb_pixels = self.width * self.height
        self.threshold = threshold
        self.isRecording = False
        self.trigger_time = 0 #Hold timestamp of the last detection
        
        if showWindows:
            cv.NamedWindow("Image")
            cv.CreateTrackbar("Detection treshold: ", "Image", self.threshold, 100, self.onChange)
        
    def run(self):
        started = time.time()
        while True:
            
            curframe = cv.QueryFrame(self.capture)
            instant = time.time() #Get timestamp o the frame
            
            self.processImage(curframe) #Process the image
            
            if self.somethingHasMoved():
                self.trigger_time = instant #Update the trigger_time
                if instant > started +5:#Wait 5 second after the webcam start for luminosity adjusting etc..
                    print datetime.now().strftime("%b %d, %H:%M:%S"), "Something is moving !"
		    os.system("cvlc --play-and-exit --fullscreen ./movie.mp4")
		    started = time.time()
            
            if self.show:
                cv.ShowImage("Image", curframe)
                cv.ShowImage("Res", self.res)
                
            cv.Copy(self.frame2gray, self.frame1gray)
            c=cv.WaitKey(1) % 0x100
            if c==27 or c == 10: #Break if user enters 'Esc'.
                break            
    
    def processImage(self, frame):
        cv.CvtColor(frame, self.frame2gray, cv.CV_RGB2GRAY)
        
        #Absdiff to get the difference between to the frames
        cv.AbsDiff(self.frame1gray, self.frame2gray, self.res)
        
        #Remove the noise and do the threshold
        cv.Smooth(self.res, self.res, cv.CV_BLUR, 5,5)
        cv.MorphologyEx(self.res, self.res, None, None, cv.CV_MOP_OPEN)
        cv.MorphologyEx(self.res, self.res, None, None, cv.CV_MOP_CLOSE)
        cv.Threshold(self.res, self.res, 10, 255, cv.CV_THRESH_BINARY_INV)

    def somethingHasMoved(self):
        nb=0 #Will hold the number of black pixels

        for x in range(self.height): #Iterate the hole image
            for y in range(self.width):
                if self.res[x,y] == 0.0: #If the pixel is black keep it
                    nb += 1
        avg = (nb*100.0)/self.nb_pixels #Calculate the average of black pixel in the image
        print(avg,"percent\n")
        if avg > self.threshold:#If over the ceiling trigger the alarm
	    print("move\n")
            return True
        else:
	  print("no move\n")
          return False
        
if __name__=="__main__":
    detect = MotionDetectorInstantaneous()
    detect.run()
