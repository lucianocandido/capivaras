import cv2
import numpy as np
from time import sleep as sl
# Create point matrix get coordinates of mouse click on image
x=y=0
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        x=x
        y=y
        print ("here", x,y)


#Initiating the webcam ### 0 or 1 for choose camera
cam = cv2.VideoCapture(1)

#cv2.namedWindow("name of window")
cv2.namedWindow("LIVE")

img_counter = 0
#img = cv2.imread('opencv_frame_0.png')
#cv2.imshow("LIVE", frame)
#Capturing frames and showing as a video
while True:
    ret, frame = cam.read()
    # Gettingf the width and height of the feed
    height = int(cam.get(4))
    width = int (cam.get(3))
    #print (width,height)
    
    # Drawing square on the webcam feed
    cv2.line(frame, (100,200), (100,300),(0,255,255))
    cv2.line(frame, (200,200), (200,300),(0,255,255))
    cv2.line(frame, (100,200), (200,200),(0,255,255))
    cv2.line(frame, (100,300), (200,300),(0,255,255))
    

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("LIVE", frame)
    #cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("LIVE", mousePoints) #get the mouse x,y pixels from a image
    #sl(1)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()