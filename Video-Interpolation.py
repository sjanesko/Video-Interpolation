from PIL import Image
import numpy as np
import cv2

cap = cv2.VideoCapture('clouds1.mp4')

width  = cap.get(3)  
height = cap.get(4)
frameCount =  cap.get(7)

print(width, height, frameCount)

average = np.zeros((int(height), int(width), 3), np.float)

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        imageArray = np.array(frame, dtype=np.float)
        average = average + imageArray / frameCount

    else:
        cap.release()
        break
    
arr = np.array(np.round(average), dtype=np.uint8)
out = Image.fromarray(arr, mode="RGB")
out.show()

input()
