import cv2
 
 
def on_change(value):
    print(value)
 
 
img= cv2.imread('D:/OneDrive/00_UNI_STUFF/THE_FLOOD/nicoTest/01.jpg')
 
windowName= 'image'
 
cv2.imshow( windowName, img)
cv2.createTrackbar('slider', windowName, 0, 100, on_change)
 
cv2.waitKey(0)
cv2.destroyAllWindows()