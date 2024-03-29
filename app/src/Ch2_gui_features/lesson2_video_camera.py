import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# check the frame width and height respectively
print(cap.get(3))
print(cap.get(4))

cap.set(3, 1320)
cap.set(4, 1240)

print(cap.get(3))
print(cap.get(4))

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    print(cap.get(3))
    print(cap.get(4))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
