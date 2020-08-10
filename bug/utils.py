import cv2
import numpy as np


def lookForTarget(Compare,Target):
    copy_image = Compare.copy()
    gray_img = cv2.cvtColor(Compare,cv2.COLOR_BGR2GRAY)
    
    template = cv2.cvtColor(Target, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(copy_image, pt, (pt[0] + w, pt[1]+h), (0,255,0),3)

    return copy_image

def lookForTargetMessage(Compare,Target, Objetivo):
    flag = False
    img = Compare
    img2 = img.copy()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(Target, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img2, pt, (pt[0] + w, pt[1]+h), (0,255,0),3)
        


    differences = cv2.subtract(Compare,Compare)
    
    print(flag)
    if flag is True:
        return 'El tornillo esta'
    else:
       return 'El tornillo no esta'
