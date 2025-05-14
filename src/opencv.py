# import cv2 library
import cv2

# Capture the webcam. 0 is the internal camera and 1 ia for an external camera
webcam = cv2.VideoCapture(0)
while True:
    ret,frame = webcam.read()

    if ret == True:
        flipped_frame = cv2.flip(frame, 1)
        cv2.imshow("VidCapture", flipped_frame)
        key = cv2.waitKey(1)
        # For now click q to close the window
        if key == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()