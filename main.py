import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

#Bat camera cua may tinh
video = VideoStream(src=0).start()

#Chứa điểm người dùng chọn để tạo đa giác
points = []

#new model
model = YoloDetect()


def handle_left_click(event, x,y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x,y])
#Vẽ các điểm người dùng đã click
def draw_polygon(frame,points):
    for point in points:
        frame =  cv2.circle(frame,(point[0],point[1]), 5,(0,0,225), -1)

    frame = cv2.polylines(frame,[np.int32(points)],False,(255,0,0),thickness=2)
    return frame

detect = False
while True:
    #Doc camera va xoay camera
    frame = video.read()
    frame = cv2.flip(frame, 1)

    #Ve ploygon
    frame = draw_polygon(frame, points)

    if detect:
        frame = model.detect(frame = frame,points = points)
   
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        points.append(points[0])
        detect = True

     # Hien thi
    cv2.imshow('Intrusion Warning', frame)
    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)
    

video.stop()
cv2.destroyAllWindows()