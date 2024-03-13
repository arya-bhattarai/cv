import cv2
import numpy as np

img = cv2.imread(r"C:\\Users\\ayrab\\OneDrive\\Desktop\\CV\\OIP.jpeg")
kernel = np.ones((5,5),np.uint8)


imgdilation = cv2.dilate(img,kernel,iterations=1) #cv2.dilate(src, dst, kernel) 
imgerosion = cv2.erode(img,kernel,iterations=1) #cv2.erode(src, dst, kernel) 
cv2.imshow('Dilation',imgdilation)
cv2.imshow('Erosion',imgerosion)
cv2.imshow('Image', img)



cv2.waitKey(0)