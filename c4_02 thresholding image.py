import cv2
 
# Reading the image
image = cv2.imread('apple.png',cv2.IMREAD_GRAYSCALE)
 
# Showing the image
cv2.imshow('Original', image)

# Applying the threshold
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('THRESH_BINARY', thresh1)

ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('THRESH_BINARY_INV', thresh2)

ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('THRESH_TRUNC', thresh3)

ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('THRESH_TOZERO', thresh4)

ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('THRESH_TOZERO_INV', thresh5)
 
cv2.waitKey()
cv2.destroyAllWindows()