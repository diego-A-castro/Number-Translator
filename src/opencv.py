# import cv2 library
import cv2
import mediapipe as mp
import numpy as np

def count_fingers(hand_landmarks):
    finger_tips = [8,12,16,20]
    fingers_up = 0
    if hand_landmarks[finger_tips].y > hand_landmarks[finger_tips - 2].y:
        fingers_up += 1

    if hand_landmarks[4].x < hand_landmarks[1].x:
        fingers_up += 1

    return fingers_up

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
            fingers_up = count_fingers(landmarks)
            mp_drawings.draw_landmarks(frame, landmarks, connections=mp_hands.HAND_CONNECTIONS)

            cv2.putText(np.zeros((500, 500, 3), dtype=np.uint8), 'Fingers: {fingers_up}', (50, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)


    if ret == True:
        flipped_frame = cv2.flip(frame, 1)
        cv2.imshow("VidCapture", flipped_frame)
        key = cv2.waitKey(1)
        # For now click q to close the window
        if key == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
