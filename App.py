import tkinter
from tkinter import filedialog
import cv2
import os
import PIL.Image, PIL.ImageTk

# PLAN: Display original video and interpolated video AFTER processed

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # set delay of video stream
        self.delay = 10

        # create open file button
        self.btn_openfile = tkinter.Button(window, text="Open file", width=50, command=self.openfile)
        self.btn_openfile.pack(anchor=tkinter.CENTER, side="top", expand=True)

        #create start button 
        self.btn_openfile = tkinter.Button(window, text="Start", width=25, command=self.update)
        self.btn_openfile.pack(anchor=tkinter.CENTER, side="top", expand=True)

        # Create a canvas that can fit the above video source size
        self.canvasOrigVid = tkinter.Canvas(window, width = 480, height = 360)
        self.canvasOrigVid.pack(side="left")

        # Create a canvas that can fit the above video source size
        self.canvasInterpolatedVid = tkinter.Canvas(window, width = 480, height = 360)
        self.canvasInterpolatedVid.pack(side="right")

        # create save button 
        self.btn_snapshot=tkinter.Button(window, text="Save", width=50, command=self.save)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, side="bottom", expand=True)
        
        self.window.mainloop()

    def openfile(self):
        self.filename = filedialog.askopenfilename()
        self.filename_base =  os.path.splitext(os.path.basename(self.filename))[0]
        self.vid = vidCapture(self.filename)

    def save(self):
        pass
    
    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.image = PIL.Image.fromarray(frame).resize((480,360))
            self.photo = PIL.ImageTk.PhotoImage(image = self.image)
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

class vidCapture:
    def __init__(self, video=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video)

        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video)

        # Get video source width and height
        self.width  = int(self.vid .get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid .get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frameCount =  self.vid .get(cv2.CAP_PROP_FRAME_COUNT)
        self.frameRate = self.vid .get(cv2.CAP_PROP_FPS)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)       

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class VidInterpolator:
    pass

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Video Interpolation")
