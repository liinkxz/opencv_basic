import cv2
 
# Reading the image
image = cv2.imread('apple.png')
 
# Showing the image
cv2.imshow('Original', image)

# Applying the filter
smoothimg = cv2.blur(image, (5, 5))
cv2.imshow('AvarageBlur', smoothimg)

smoothimg = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('GaussianBlur', smoothimg)

smoothimg = cv2.bilateralFilter(image, 5, 75, 75)
cv2.imshow('bilateralFilter', smoothimg)

smoothimg = cv2.medianBlur(image, 5)
cv2.imshow('medianBlur', smoothimg)

 
cv2.waitKey()
cv2.destroyAllWindows()
