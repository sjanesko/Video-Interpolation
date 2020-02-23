import cv2

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
        self.window.mainloop()