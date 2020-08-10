import cv2
import numpy as np


def lookForTarget(Compare,Target):
    global  mensaje
    copy_image = Compare.copy()
    gray_img = cv2.cvtColor(Compare,cv2.COLOR_BGR2GRAY)
    
    template = cv2.cvtColor(Target, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(copy_image, pt, (pt[0] + w, pt[1]+h), (0,255,0),3)
    diff = cv2.absdiff(Compare, copy_image)
    result =  not np.any(diff) 
    
    if result is True:
        #no esta el target
        mensaje = 'El objetivo no esta'
        return Compare
        
    else:
        #si esta el target
        mensaje = 'El objetivo esta'
        return copy_image


def lookForTargetMessage():
    global mensaje
    return mensaje
