import cv2 as cv
from utils import _bin_range


class Checker:
    def __init__(self) -> None:
        pass

    def Check():
        pass


class Concrete(Checker):
    def __init__(self, pixel, frame, hamma) -> None:
        super().__init__()
        self.pixel, self.frame, self.hamma = pixel, frame, hamma
        pass

    def Check(self):
        if self.pixel > (2050000,0,0,0):
            bin = _bin_range(self.frame, type='Бетон')
            cv. imshow ('bin', bin)
            print ("Показания камеры: Бетон")
            self.hamma += 1
        else :
            bin = _bin_range(self.frame, type='Щебень')
            cv. imshow ('bin', bin)
            self.pixel = cv.sumElems (bin)
        
        return self.pixel, self.hamma


class Sheb(Checker):
    def __init__(self, pixel, frame, hamma) -> None:
        super().__init__()
        self.pixel, self.frame, self.hamma = pixel, frame, hamma

    def Check(self):
        if self.pixel > (130000,0,0,0):
            print ("Показания камеры: Щебень")
            self.hamma += 1
        else :
            bin = _bin_range(self.frame, type='Асфальт')
            cv. imshow ('bin', bin)
            self.pixel = cv.sumElems (bin)
    
        return self.pixel, self.hamma



class Asphalt(Checker):
    def __init__(self, pixel, frame, hamma) -> None:
        super().__init__()
        self.pixel, self.frame, self.hamma = pixel, frame, hamma

    def Check(self):
        if self.pixel > (210000,0,0,0):
            print ("Показания камеры: Асфальт")
        else :
            bin = _bin_range(self.frame, type='Грунт')
            cv. imshow ('bin', bin)
            self.pixel = cv.sumElems (bin)  
        
        return self.pixel, self.hamma



class Grunt(Checker):
    def __init__(self, pixel, frame, hamma) -> None:
        super().__init__()
        self.pixel, self.frame, self.hamma = pixel, frame, hamma

    def Check(self):
        if self.pixel > (320000,0,0,0):
            print ("Показания камеры: Грунт")
            self.hamma += 1
        else :
            print ("Показания камеры: Неизвестное покрытие")
            self.hamma += 1
        
        return self.pixel, self.hamma
