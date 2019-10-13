import cv2
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
video = cv2.VideoCapture(0)
while video.isOpened():
    success, image =video.read()
    gray_converted = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    eye_ = eye_cascade.detectMultiScale(gray_converted, 1.2, 4)
    for (x,y,w,h) in eye_:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0),2)
        cv2.imshow('Detection',image)
    video.release()
    cv2.destroyAllWindows()