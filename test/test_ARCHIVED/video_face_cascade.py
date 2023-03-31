import cv2
import sys
import time
 
cascasdepath = "/opt/ros/kinetic/share/OpenCV-3.3.1-dev/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascasdepath)
face_cascade.load(cascasdepath)

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320)
video_capture.set(4, 240)

while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()
 
    if not ret:
        break
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))
 
    #print("The number of faces found = ", len(faces))
 
    for (x,y,w,h) in faces:
#        cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)
        center = (x + w//2, y + h//2)
        if (x + w//2) < 150:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)
        elif (x + w//2) > 170:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (0, 0, 255), 2)
        else:
            cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 2)
        time.sleep(0.2)
        print(center, w//2)
        if w//2 > 50:
            video_capture.release()
            break

 
    cv2.imshow("Faces found", image)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
