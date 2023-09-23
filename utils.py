import cv2

def nothing(x): 
    pass 

def _createTrackbar():
    cv2.namedWindow('result') 
    cv2.resizeWindow ('result', 1200, 1200)
    cv2.createTrackbar('minb','result',0,255, nothing) 
    cv2.createTrackbar('ming','result',0,255, nothing) 
    cv2.createTrackbar('minr','result',0,255, nothing) 

    cv2.createTrackbar('maxb','result',0,255, nothing) 
    cv2.createTrackbar('maxg','result',0,255, nothing) 
    cv2.createTrackbar('maxr','result',0,255, nothing) 

def min_RGB():
    minb=cv2.getTrackbarPos('minb','result')
    ming=cv2.getTrackbarPos('ming','result')
    minr=cv2.getTrackbarPos('minr','result')
    return minb, ming, minr

def max_RGB():
    maxb=cv2.getTrackbarPos('maxb','result')
    maxg=cv2.getTrackbarPos('maxg','result')
    maxr=cv2.getTrackbarPos('maxr','result')

    return maxb, maxg, maxr


def _bin_range(frame, type='Асфальт'): ## Диапозон при бинаризации. Выявлен эмпирически 
    return cv2.inRange (frame, (65,55,55), (129,124,100)) if type == 'Асфальт' else \
        cv2.inRange(frame, (125,120,120), (150,150,150)) if type == 'Бетон' else \
        cv2.inRange (frame, (93,117,153), (139,153,182)) if type == 'Грунт' else \
        cv2.inRange (frame, (204,190,191), (230,235,235)) if type == 'Щебень' else \
        cv2.inRange (frame, (0,0,0), (255,255,255))