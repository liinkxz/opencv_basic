import cv2
 
# Reading the image
image = cv2.imread('morph.png',cv2.IMREAD_GRAYSCALE)
 
# Showing the image
cv2.imshow('Original', image)

# Applying the morph
morph = cv2.dilate(image,(5,5),iterations = 3)
cv2.imshow('dilate', morph)

morph = cv2.erode(image,(5,5),iterations = 3)
cv2.imshow('erode', morph)

morph = cv2.morphologyEx(image, cv2.MORPH_OPEN, (5,5))
cv2.imshow('MORPH_OPEN', morph)

morph = cv2.morphologyEx(image, cv2.MORPH_CLOSE, (5,5))
cv2.imshow('MORPH_CLOSE', morph)

morph = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, (5,5))
cv2.imshow('MORPH_GRADIENT', morph)
 
cv2.waitKey()
cv2.destroyAllWindows()
