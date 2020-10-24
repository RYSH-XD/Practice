# plot bbox for oriented bbox detection
# bbox information should be saved in a txt file and follow the below format in each row: 
# class x1 y1 x2 y2 x3 y3 x4 y4
import cv2 as cv
import os

image_root_dir='path to image'
label_root_dir='path to label'
labeled_image_root_dir='path to result'

if not os.path.exists(labeled_image_root_dir):
    os.makedirs(labeled_image_root_dir)

#image_root_list=os.listdir(image_root_dir)
label_root_list=os.listdir(label_root_dir)

for i,name in enumerate(label_root_list):
    print ('plot '+name)
    
    img=cv.imread(image_root_dir+'/'+name[:-4]+'.png')
    f = open(label_root_dir+'/'+name,'r')
    for line in open(label_root_dir+'/'+name):
            
        class_name=line.split(' ')[0]
        coordinate=[]
        coordinate.append(int(line.split(' ')[1]))
        coordinate.append(int(line.split(' ')[2]))
        coordinate.append(int(line.split(' ')[3]))
        coordinate.append(int(line.split(' ')[4]))
        coordinate.append(int(line.split(' ')[5]))
        coordinate.append(int(line.split(' ')[6]))
        coordinate.append(int(line.split(' ')[7]))
        coordinate.append(int(line.split(' ')[8]))
        for counter in range(3):
            counter=counter*2
            ptStart = (coordinate[counter], coordinate[counter+1])
            ptEnd = (coordinate[counter+2], coordinate[counter+3])
            point_color = (0, 255, 0) # BGR
            thickness = 1 
            lineType = 4
            cv.line(img, ptStart, ptEnd, point_color, thickness, lineType)
        #counter=3:
        ptStart = (coordinate[6], coordinate[7])
        ptEnd = (coordinate[0], coordinate[1])
        point_color = (0, 255, 0) # BGR
        thickness = 1 
        lineType = 4
        cv.line(img, ptStart, ptEnd, point_color, thickness, lineType)
        #lable name
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, class_name_config, (coordinate[0], coordinate[1]), font, 0.5, (0, 0, 255), 1)

    f.close()
    cv.imwrite(labeled_image_root_dir+'/'+name[:-4]+'.png', img)
    
