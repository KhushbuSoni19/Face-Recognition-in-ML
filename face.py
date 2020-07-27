#import cv2
import numpy as np
#import os
from sklearn.neighbors import KNeighborsClassifier

data = np.load("face_data.npy")
print(data.shape, data.dtype)

X = data[:, 1:].astype(int)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit()
'''
cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
name = input("enter your name")

frames = []
outputs = []
while True:
    ret, frame = cap.read()

    if ret:
        faces = detector.detectMultiScale(frame)
        for face in faces:
            x, y, w, h = face
            cut = frame[y:y+h, x:x+w]

            fix = cv2.resize(cut, (200, 200))
            gray = cv2.cvtColor(fix, cv2.COLOR_BGR2GRAY)

        cv2.imshow("my screen", frame)
        cv2.imshow("my face", gray)

    key = cv2.waitKey(1)
    if key == ord("k"):
        break
    if key == ord("q"):
        cv2.imwrite(name +".jpg", frame)
        frames.append(gray.flatten())
        outputs.append([name])

X = np.array(frames)
y = np.array(outputs)

data = np.hstack([y, X])

f_name = "face_data.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    data = np.vstack([old, data])


np.save(f_name, data)

#print(data.shape)

cap.release()
cv2.destroyAllWindows()
'''