import cv2
import sys
import time
import RPi.GPIO as GPIO

cascasdepath = "/opt/ros/kinetic/share/OpenCV-3.3.1-dev/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascasdepath)

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320)
video_capture.set(4, 240)

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

L1=16
L2=19
R1=20
R2=26
enL=3
enR=2


GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(enL, GPIO.OUT)
GPIO.setup(enR, GPIO.OUT)

power_left = GPIO.PWM(enL, 100)
power_right = GPIO.PWM(enR, 100)
##power_left.start(40)
##power_right.start(40)

def forward():
    power_left.start(40)
    power_right.start(40)
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)
    
def reverse():
    power_left.start(40)
    power_right.start(40)
    GPIO.output(L2, GPIO.HIGH)
    GPIO.output(R2, GPIO.HIGH)

def left():
    power_left.start(40)
    power_right.start(50)
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)

def right():
    power_left.start(50)
    power_right.start(40)
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)
    
def fastleft():
##    power_left.start(50)
##    power_right.start(50)
    GPIO.output(L2, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)
    
def fastright():
##    power_left.start(50)
##    power_right.start(50)
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R2, GPIO.HIGH)

def stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)
    
while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()
 
    if not ret:
        break
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (30,30))
 
    #print("The number of faces found = ", len(faces))
 
    for (x,y,w,h) in faces:
#        cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)
        center = (x + w//2, y + h//2)
        middle_position = 160
        limit = 55
        
        cv2.rectangle(image,(140,240), (180,0),(0,255,0),1)
        
        if (x + w//2) < middle_position - 15:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)
            left()
            
        elif (x + w//2) > middle_position + 15:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (0, 0, 255), 2)
            right()
            
        else:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 2)
            forward()
            
        time.sleep(0.2)
        stop()
        print(center, w//2)
        
        if w//2 > limit:
            stop()
            reverse()
            time.sleep(0.1)
            GPIO.cleanup()
            video_capture.release()
            break

 
    cv2.imshow("Faces found", image)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
