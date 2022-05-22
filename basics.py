import cv2
import face_recognition
import numpy as np

imgsrk = face_recognition.load_image_file('imagesbasics/srk.jpg')
imgsrk= cv2.cvtColor(imgsrk,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('imagesbasics/srk test.jpg')
imgtest= cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc= face_recognition.face_locations(imgsrk)[0]
encodesrk= face_recognition.face_encodings(imgsrk)[0]
cv2.rectangle(imgsrk,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

faceloctest= face_recognition.face_locations(imgtest)[0]
encodetest= face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)

results= face_recognition.compare_faces([encodesrk],encodetest)
faceDis = face_recognition.face_distance([encodesrk],encodetest)
print(results,faceDis)
cv2.putText(imgtest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('SHAHRUKH',imgsrk)
cv2.imshow('SHAHRUKH test',imgtest)
cv2.waitKey(0)