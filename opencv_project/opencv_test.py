# import cv2
# import numpy as np
#
# def showImage():
#     imgfile = 'images/model.png'
#     img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
#
#     cv2.imshow('model', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# showImage()

import cv2
cap = cv2.VideoCapture(0) #0 or -1
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv2.imshow('camera-0', img)
        if cv2.waitKey(1) & 0xFF == 27: #esc
            break
    else:
        print('no camera!')
        break
cap.release()
cv2.destroyAllWindows()

