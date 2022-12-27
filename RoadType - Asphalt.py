import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


## Ввод видео
cap=cv.VideoCapture ("video\\AsphaltRandExp2.mp4")
x = []
y = []
n = 0
delta = 0
hamma = 0

while (True) :
    ret,frame=cap.read ()
    frame = cv.resize (frame, (120,120))
    cv. imshow ('frame', frame)  
    
    ## Диапозон при бинаризации
    
    Asphalt = cv.inRange (frame, (65,55,55), (129,124,100)) ## Асфальт
    Concrete = cv.inRange(frame, (125,120,120), (150,150,150)) ## Бетон
    Grunt = cv.inRange (frame, (93,117,153), (139,153,182)) ## Грунт
    Sheb = cv.inRange (frame, (204,190,191), (230,235,235)) ## Щебень

    bin = Asphalt
    bin = cv.resize (bin, (120,120))
    cv. imshow ('bin', bin)



    f = open('SensorData\\Asphalt30.txt', encoding="utf-8")
    for line in f :
        y.append(float (line.rstrip('\n')))
        n +=1
        x.append(n)
        #plt.plot(x, y, color="blue")
        #plt.pause(0.05)
        A = max (y)
        if  0.11 < A < 0.15  :
            print ("Показания датчика: Асфальт")
            delta += 1

        pixel = cv.sumElems (bin)
        if pixel > (2050000,0,0,0):
            bin = Concrete
            cv. imshow ('bin', bin)
            print ("Показания камеры: Бетон")
            hamma += 1
        else :
            bin = Sheb
            cv. imshow ('bin', bin)
            pixel = cv.sumElems (bin)
            if pixel > (130000,0,0,0):
                print ("Показания камеры: Щебень")
                hamma += 1
            else :
                bin = Asphalt
                cv. imshow ('bin', bin)
                pixel = cv.sumElems (bin)
                if pixel > (210000,0,0,0):
                    print ("Показания камеры: Асфальт")
                else :
                    bin = Grunt
                    cv. imshow ('bin', bin)
                    pixel = cv.sumElems (bin)                   
                    if pixel > (320000,0,0,0):
                        print ("Показания камеры: Грунт")
                        hamma += 1
                    else :
                        print ("Показания камеры: Неизвестное покрытие")
                        hamma += 1
    Ver = hamma/delta
    print ('Вероятность ошибки камеры = ', Ver)
        
    if cv.waitKey (10) & 0xFF == ord('q') :
        break


cv.destroyAllWindows
    