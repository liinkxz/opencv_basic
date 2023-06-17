import cv2

face_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_eye.xml')
cat_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalcatface_extended.xml')

img = cv2.imread('family.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.5, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cats = cat_cascade.detectMultiScale(gray)
for (sx,sy,sw,sh) in cats:
    img = cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()