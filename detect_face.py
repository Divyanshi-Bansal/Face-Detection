import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

videoCapture = cv2.VideoCapture(0)

while True:
    rect , frame = videoCapture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=5, minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2)

    cv2.imshow('Video' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()























face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('PHOTO.JPG')

#this method is work for only gray scale images that's why
#we convert our image into gray
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#try to detect the faces
faces = face_cascade.detectMultiScale(gray,  1.1, 4 )

for (x,y,w,h) in faces:
    cv2.rectangle(img ,  (x,y)  ,(x+w , y+h) , (255 , 0 , 0) , 2 )

cv2.imshow('img' , img)
cv2.waitKey()