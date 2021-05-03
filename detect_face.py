import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# #sets the video source to the default webcam
videoCapture = cv2.VideoCapture(0)

while True:
    ret , frame = videoCapture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray ,1.1 , 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2)

    cv2.imshow('Video' , frame)

    #for exiting--escape key--30 ascii value
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


videoCapture.release()


