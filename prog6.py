import cv2
import numpy as np

img = cv2.imread(r"C:\\Users\\ayrab\\OneDrive\\Desktop\\CV\\OIP.jpeg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgrgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('Image', img)
cv2.imshow('Grayscale', gray_image)
cv2.imshow('BGR to RGB', imgrgb)


cv2.waitKey(0)