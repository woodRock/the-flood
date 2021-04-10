# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.widgets import Slider, Button
import cv2

img= cv2.imread('D:/OneDrive/00_UNI_STUFF/THE_FLOOD/nicoTest/01.jpg')
imgMap= img.copy() #cv2.imread('D:/OneDrive/00_UNI_STUFF/THE_FLOOD/nicoTest/01.jpg')
print( imgMap)
#imgMap= mpimg.imread( 'D:\\OneDrive\\00_UNI_STUFF\\THE_FLOOD\\nicoTest\\01.jpg')
hh= len( imgMap)
ww= len( imgMap[ 0])
SLIDE= 10

def on_change( value):
    cv2.imshow( windowName, drawMap( value))
    #print(value)

def drawMap( val):
    imgMap= img.copy()
    for i in range( len( imgMap)):
        for j in range( len( imgMap[ i])):
            newVal= imgMap[ i][ j][ 0]
            if newVal< val: imgMap[ i][ j]=[ 255, 122, 0]
            j+= 1
        i+= 1
    return imgMap

windowName= 'myMap'
 
cv2.imshow( windowName, imgMap)#drawMap( SLIDE))
cv2.createTrackbar( 'slider', windowName, 0, 255, on_change)
 
cv2.waitKey( 0)
cv2.destroyAllWindows()