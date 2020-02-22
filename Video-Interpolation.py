from PIL import Image
import numpy as np
import cv2
import glob
from matplotlib import pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

def averageFrame(frame1, frame2, width, height):
    average = np.zeros((width, height, 3), np.float)
    imageArray1 = np.array(frame1, dtype=np.float)
    imageArray2 = np.array(frame2, dtype=np.float)
    average = (imageArray1 + imageArray2) / 2 
    return np.array(np.round(average), dtype=np.uint8)

if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    fileNameOnly = os.path.splitext(os.path.basename(filename))[0]

    cap = cv2.VideoCapture(filename)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frameCount =  cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frameRate = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("output/" + str(fileNameOnly) + "-i.mp4", fourcc, frameRate * 2 - 1, (width, height))

    count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            if (count < frameCount - 1):
                # write first frame 
                out.write(frame)

                # save frame location and frame into temp variable 
                currentCapIndex = cap.get(cv2.CAP_PROP_POS_FRAMES)
                currentFrame = frame

                #load next frame location
                ret, nextFrame = cap.read()

                #go back to original frame
                cap.set(cv2.CAP_PROP_POS_FRAMES, currentCapIndex)

                # write inserted average frame 
                insertFrame = averageFrame(currentFrame, nextFrame, width, height)
                out.write(insertFrame)            
                count += 1

            else:        
                out.write(frame)
                break
        else:
            cap.release()
            break

    out.release()
        