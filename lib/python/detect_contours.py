import cv2.cv as cv
import os
from datetime import datetime
import time

class MotionDetectorAdaptative():
    
    def onChange(self, val): #callback when the user change the detection threshold
        self.threshold = val
    
    def __init__(self,threshold=20, showWindows=False):
        self.writer = None
        self.font = None
        self.show = showWindows #Either or not show the 2 windows
        self.frame = None
        root_path = os.path.dirname(
                            os.path.dirname(os.path.abspath(__file__)))
        os.chdir(os.path.join(root_path, "etc", "video"))
        self.capture=cv.CaptureFromCAM(0)
        self.frame = cv.QueryFrame(self.capture) #Take a frame to init recorder
        
        self.gray_frame = cv.CreateImage(cv.GetSize(self.frame), cv.IPL_DEPTH_8U, 1)
        self.average_frame = cv.CreateImage(cv.GetSize(self.frame), cv.IPL_DEPTH_32F, 3)
        self.absdiff_frame = None
        self.previous_frame = None
        
        self.surface = self.frame.width * self.frame.height
        self.currentsurface = 0
        self.currentcontours = None
        self.threshold = threshold
        self.isRecording = False
        self.trigger_time = 0 #Hold timestamp of the last detection
        
        if showWindows:
            cv.NamedWindow("Image")
            cv.CreateTrackbar("Detection treshold: ", "Image", self.threshold, 100, self.onChange)
        

    def run(self):
        started = time.time()
        while True:
            
            currentframe = cv.QueryFrame(self.capture)
            instant = time.time() #Get timestamp o the frame
            
            self.processImage(currentframe) #Process the image
            
            if not self.isRecording:
                if self.somethingHasMoved():
                    self.trigger_time = instant #Update the trigger_time
                    if instant > started +10:#Wait 5 second after the webcam start for luminosity adjusting etc..
			print datetime.now().strftime("%b %d, %H:%M:%S"), "Something is moving !"
		    	os.system("cvlc --play-and-exit --equalizer-preamp=20 --fullscreen ./v1.mp4")
			os.system("mv v1.mp4 vt.mp4")
			os.system("mv v2.mp4 v1.mp4")
			os.system("mv v3.mp4 v2.mp4")
			os.system("mv v4.mp4 v3.mp4")
			os.system("mv v5.mp4 v4.mp4")
			os.system("mv v6.mp4 v5.mp4")
			os.system("mv v7.mp4 v6.mp4")
			os.system("mv v8.mp4 v7.mp4")
			os.system("mv v9.mp4 v8.mp4")
			os.system("mv v10.mp4 v9.mp4")
			os.system("mv vt.mp4 v10.mp4")
		    	instant = time.time() #Get timestamp o the frame
		    	started = instant
		    	currentframe = cv.QueryFrame(self.capture)
                    	self.processImage(currentframe) #Process the image
                        print "Something is moving !"
                        
                cv.DrawContours (currentframe, self.currentcontours, (0, 0, 255), (0, 255, 0), 1, 2, cv.CV_FILLED)
            
            if self.show:
                cv.ShowImage("Image", currentframe)
                
            c=cv.WaitKey(1) % 0x100
            if c==27 or c == 10: #Break if user enters 'Esc'.
                break
    
    def processImage(self, curframe):
            cv.Smooth(curframe, curframe) #Remove false positives
            
            if not self.absdiff_frame: #For the first time put values in difference, temp and moving_average
                self.absdiff_frame = cv.CloneImage(curframe)
                self.previous_frame = cv.CloneImage(curframe)
                cv.Convert(curframe, self.average_frame) #Should convert because after runningavg take 32F pictures
            else:
                cv.RunningAvg(curframe, self.average_frame, 0.05) #Compute the average
            
            cv.Convert(self.average_frame, self.previous_frame) #Convert back to 8U frame
            
            cv.AbsDiff(curframe, self.previous_frame, self.absdiff_frame) # moving_average - curframe
            
            cv.CvtColor(self.absdiff_frame, self.gray_frame, cv.CV_RGB2GRAY) #Convert to gray otherwise can't do threshold
            cv.Threshold(self.gray_frame, self.gray_frame, 50, 255, cv.CV_THRESH_BINARY)

            cv.Dilate(self.gray_frame, self.gray_frame, None, 15) #to get object blobs
            cv.Erode(self.gray_frame, self.gray_frame, None, 10)

            
    def somethingHasMoved(self):
        
        # Find contours
        storage = cv.CreateMemStorage(0)
        contours = cv.FindContours(self.gray_frame, storage, cv.CV_RETR_EXTERNAL, cv.CV_CHAIN_APPROX_SIMPLE)

        self.currentcontours = contours #Save contours
        
        while contours: #For all contours compute the area
            self.currentsurface += cv.ContourArea(contours)
            contours = contours.h_next()
        
        avg = (self.currentsurface*100)/self.surface #Calculate the average of contour area on the total size
        self.currentsurface = 0 #Put back the current surface to 0
        
        if avg > self.threshold:
            return True
        else:
            return False

        
if __name__=="__main__":
    detect = MotionDetectorAdaptative()
    detect.run()
