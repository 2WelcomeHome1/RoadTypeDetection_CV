import numpy as np
import cv2 as cv
from RoadType import *



class RoadTypeDetector:
    def __init__(self) -> None:
        self.cap=cv.VideoCapture ("video\\AsphaltRandExp2.mp4")
        self.sensor_data = open('SensorData\\Asphalt30.txt', encoding="utf-8")
        self.y = []
        self.delta = 0
        self.hamma = 0
        pass

    def _bin_range(self, frame, type='Асфальт'): ## Диапозон при бинаризации. Выявлен эмпирически 
        return cv.inRange (frame, (65,55,55), (129,124,100)) if type == 'Асфальт' else \
            cv.inRange(frame, (125,120,120), (150,150,150)) if type == 'Бетон' else \
            cv.inRange (frame, (93,117,153), (139,153,182)) if type == 'Грунт' else \
            cv.inRange (frame, (204,190,191), (230,235,235)) if type == 'Щебень' else \
            cv.inRange (frame, (0,0,0), (255,255,255))
    
    def _show_real_image(self, frame):
        frame = cv.resize (frame, (120,120))
        cv. imshow ('frame', frame)  
        
        return frame
    
    def _show_segmented_image(self, frame):
        bin = cv.resize (self._bin_range(frame, type='Асфальт'), (120,120))
        cv. imshow ('bin', bin)

        return bin
    
    def get_sensor_data(self, line):
        self.y.append(float (line.rstrip('\n')))
        A = max (self.y)
        if  0.11 < A < 0.15  :
            print ("Показания датчика: Асфальт")
            self.delta += 1

    def check_camera_data(self, pixel, frame, hamma):
        concrete = Concrete(pixel, frame, hamma)
        pixel, hamma = concrete.Check()

        sheb = Sheb(pixel, frame, hamma)
        pixel, hamma = sheb.Check()

        asphalt = Asphalt(pixel, frame, hamma)
        pixel, hamma = asphalt.Check()

        grunt = Grunt(pixel, frame, hamma)
        pixel, hamma = grunt.Check()

        return hamma       

    def detector(self, frame, bin):
        pixel = cv.sumElems (bin)
        self.hamma = self.check_camera_data(pixel, frame, self.hamma)

    def comparator(self, frame, bin):
        for line in self.sensor_data :
            self.get_sensor_data(line)
            pixel = cv.sumElems (bin)
            self.hamma = self.check_camera_data(pixel, frame, self.hamma)
        
        Ver = self.hamma/self.delta
        print ('Вероятность ошибки камеры = ', Ver)

    def run(self, mode = 'comparator'):
        while True:
            _,frame=self.cap.read ()
            frame = self._show_real_image(frame)
            bin = self._show_segmented_image(frame)
            self.comparator(frame, bin) if mode == 'comparator' else  self.detector(frame, bin)        
            if cv.waitKey (10) & 0xFF == ord('q') : break

        self.cap.release ()
        cv.destroyAllWindows
    

if __name__ == '__main__':
    RoadTypeDetector().run(mode='detector')