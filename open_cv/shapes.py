import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier('C:\\Users\\Farhan\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data')

img = cv2.imread("my.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(img_gray, 1.3, 4)
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), 2)

cv2.imshow("Face", img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()