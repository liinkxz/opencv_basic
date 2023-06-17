import cv2
import numpy as np

coins_color = cv2.imread('coins.png')
cv2.imshow("coins_color", coins_color)
coins_gray = cv2.cvtColor(coins_color, cv2.COLOR_BGR2GRAY)
_, coins_th = cv2.threshold(coins_gray, 200, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(coins_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    rect = cv2.boundingRect(cnt)
    cv2.rectangle(coins_color, rect, (0,255,0),2)

    if(rect[2] > 110):
        coin_type = "10 Bath"
    elif(rect[2] > 100):
        coin_type = "5 Bath"
    elif(rect[2] > 80):
        coin_type = "1 Bath"
    elif(rect[2] > 60):
        coin_type = "0.25 Bath"
    else:
        coin_type = ""

    cv2.putText(coins_color, coin_type, (rect[0], rect[1]), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255))

cv2.imshow("detected", coins_color)
cv2.waitKey(0)