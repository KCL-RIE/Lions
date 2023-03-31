import opencv2
import sys
import time
 
cascasdepath = "/opt/ros/kinetic/share/OpenCV-3.3.1-dev/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = opencv2.CascadeClassifier(cascasdepath)

video_capture = opencv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()
 
    if not ret:
        break
 
    gray = opencv2.cvtColor(image, opencv2.COLOR_BGR2GRAY)
 
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))
 
    #print("The number of faces found = ", len(faces))
 
    for (x,y,w,h) in faces:
#        cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)
        center = (x + w//2, y + h//2)
        if (x + w//2) < 310:
            opencv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)
        elif (x + w//2) > 330:
            opencv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (0, 0, 255), 2)
        else:
            opencv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 2)
        time.sleep(0.1)
        print(center, (w//2, h//2))
        if w//2 > 100:
            video_capture.release()
            break

 
    opencv2.imshow("Faces found", image)    

    if opencv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
opencv2.destroyAllWindows()
