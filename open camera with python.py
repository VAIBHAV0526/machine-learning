import cv2
#cv2 with web came
#we use open cv
# series of frame
cp=cv2.VideoCapture(0)
while True:
  ret,frame=cp.read()
  if ret==False:
    continue
  cv2.imshow("video Frame",frame)

  key_pre=cv2.waitKey(1) & 0xFF
  if key_pre==ord("q"):
    break
cp.release()    
cv2.destroyAllWindows()
  
