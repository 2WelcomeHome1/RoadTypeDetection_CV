import cv2
from utils import _createTrackbar, min_RGB, max_RGB


class BinarisationAlgorithm():
    def __init__(self) -> None:
        self.cap = cv2.VideoCapture ("video\\Redlight.mp4")
        _createTrackbar()
        self.Binarissation_window()
        pass
    

    def Binarissation_window(self):
        while (True):
            _,frame=self.cap.read ()
            mask = cv2.inRange(frame, (min_RGB()), (max_RGB())) 
            cv2.imshow('mask',mask)
            result = cv2.bitwise_and(frame, frame, mask = mask)
            cv2.imshow('result', result)
            if cv2.waitKey(1) == 27 :
                break
        self.cap.release ()
        cv2.destroyAllWindows

if __name__ == '__main__':
    BinarisationAlgorithm()




