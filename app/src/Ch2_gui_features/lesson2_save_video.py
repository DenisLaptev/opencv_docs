import numpy as np
import cv2

cap = cv2.VideoCapture(0)

PATH_TO_SAVE_VIDEO = '../../resources/denis.mp4'
FRAMES_PER_SECOND = 20.0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(PATH_TO_SAVE_VIDEO,
                      fourcc,
                      FRAMES_PER_SECOND,
                      (FRAME_WIDTH, FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
