import cv2
import torch
import numpy as np
import timeit
from file_support import get_list_label,write_labels_file

CONF_THRES = 0.7

name = get_list_label('label.txt')

def draw_rec(image,pos1,pos2,index,conf):
    thickness = 1
    image = cv2.rectangle(image, pos1, pos2, color_array[index], thickness)
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image,'{0} {1}'.format(name[index],conf),pos1, font, 0.25, color_array[index], 1, cv2.LINE_AA)
    return image

def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    return (x,y,w,h)

model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='best_yolo_v5.pt')
img = cv2.imread('test.jpg')
h,w = img.shape[:2]
size = (w,h)
img_org = np.copy(img)
image = img_org[:, :, ::-1]
results = model(image)
rss = results.xyxy[0]
list_labels_content = []
for rs in rss:
    xmin,ymin = int(rs[0]),int(rs[1])
    xmax,ymax = int(rs[2]),int(rs[3])
    bbox = [xmin,xmax,ymin,ymax]
    conf = round(float(rs[4]),3) 
    clss = int(rs[5])
    if(conf>CONF_THRES):
        x,y,w,h = convert_coordinates(size,bbox)
        content = f'{clss} {x} {y} {w} {h}'
        list_labels_content.append(content)
write_labels_file('test.txt',list_labels_content)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow('mat',img_org)
cv2.waitKey()
cv2.destroyAllWindows()
