# import cv2 library
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils

# Capture the webcam. 0 is the internal camera and 1 ia for an external camera
webcam = cv2.VideoCapture(0)
while True:
    ret,frame = webcam.read()

    # Apply the hand tracking model
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.Hands(max_num_hands=3, min_detection_confidence=0.7).process(frame)

    # Draw annotations on the image
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawings.draw_landmarks(frame, landmarks, connections=mp_hands.HAND_CONNECTIONS)


    if ret == True:
        flipped_frame = cv2.flip(frame, 1)
        cv2.imshow("VidCapture", flipped_frame)
        key = cv2.waitKey(1)
        # For now click q to close the window
        if key == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
