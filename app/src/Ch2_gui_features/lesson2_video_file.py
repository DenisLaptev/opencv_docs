import numpy as np
import cv2

path_to_video = '../../resources/red_panda_snow.mp4'
cap = cv2.VideoCapture(path_to_video)

print(cap.get(3))
print(cap.get(4))

cap.set(3, 1320)
cap.set(4, 1240)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
