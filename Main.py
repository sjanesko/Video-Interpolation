import tkinter
from tkinter import filedialog
import VideoCapture
import cv2
import os

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        #create button
        self.btn_openfile = tkinter.Button(window, text="Open file", width=50, command=self.openfile)
        self.btn_openfile.pack(anchor=tkinter.CENTER, expand=True)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = 400, height = 300)
        self.canvas.pack()


        self.window.mainloop()

    def openfile(self):
        self.filename = filedialog.askopenfilename()
        self.filename_base =  os.path.splitext(os.path.basename(filename))[0]
        self.vid = cv2.VideoCapture(self.filename)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Video Interpolation")
