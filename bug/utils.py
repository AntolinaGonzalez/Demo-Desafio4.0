import cv2
import numpy as np


def get_filteres_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if action == 'NO_FILTERED':
        filtered = img
    if action == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    return filtered

def lookForTarget(Compare,Target):
    #image = cv2.imread(Compare)
    copy_image = Compare.copy()
    gray_img = cv2.cvtColor(Compare,cv2.COLOR_BGR2GRAY)
    #template = cv2.imread(Target, cv2.IMREAD_GRAYSCALE)
    template = cv2.cvtColor(Target, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(copy_image, pt, (pt[0] + w, pt[1]+h), (0,255,0),3)

    #cv2.imshow('img2', img2)
    #differences = cv2.subtract(img,img2)

    #result = not np.any(differences) 

    # if result is True:
    #     print('El tornillo no esta')
    # else:
    #     print('El tornillo esta')
    return copy_image

def mensaje():
    return 'hola bebe ya ando'