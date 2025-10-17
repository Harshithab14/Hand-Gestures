import cv2
import pyautogui
from math import hypot
import mediapipe as mp
from time import time

# Initialize mediapipe pose
mp_pose = mp.solutions.pose
pose_video = mp_pose.Pose(static_image_mode=False, model_complexity=1,
                          min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def detectPose(image, pose, draw=False):
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(imageRGB)
    if results.pose_landmarks and draw:
        mp_drawing.draw_landmarks(image=image, landmark_list=results.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS)
    return image, results

def handsJoined(results, frame_width, frame_height):
    lw = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
    rw = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
    dist_ratio = hypot(lw.x - rw.x, lw.y - rw.y)
    return dist_ratio < 0.1  # Auto threshold as ratio of frame size

def checkLeftRight(results, frame_width):
    left_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x * frame_width
    right_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x * frame_width
    if left_x < frame_width // 2 < right_x:
        return "Center"
    elif right_x < frame_width // 2:
        return "Left"
    else:
        return "Right"

def checkJumpCrouch(results, frame_height, MID_Y):
    left_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * frame_height
    right_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * frame_height
    actual_mid_y = (left_y + right_y) / 2
    if actual_mid_y < MID_Y - 30:
        return "Jumping"
    elif actual_mid_y > MID_Y + 30:
        return "Crouching"
    else:
        return "Standing"

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 960)

cv2.namedWindow("Subway Surfers Pose Control", cv2.WINDOW_NORMAL)
time1 = 0

game_started = False
x_pos_index = 1  # 0 = Left, 1 = Center, 2 = Right
y_pos_index = 1  # 0 = Crouching, 1 = Standing, 2 = Jumping
MID_Y = None
counter = 0
num_of_frames = 10
calibrated = False
hand_threshold = None

print("🎮 Game control mode active! Stand in front of camera.")
print("👉 Join both hands to start the game. ESC to exit.")

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        continue
    frame = cv2.flip(frame, 1)
    height, width = frame.shape[:2]

    frame, results = detectPose(frame, pose_video, draw=True)

    if results.pose_landmarks:
        # Auto-calibrate MID_Y
        if not calibrated and handsJoined(results, width, height):
            left_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height
            right_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height
            MID_Y = (left_y + right_y) / 2
            calibrated = True
            print("🛠 Calibration done! MID_Y set.")

        if game_started:
            # Horizontal movement
            pos = checkLeftRight(results, width)
            if (pos == 'Left' and x_pos_index != 0) or (pos == 'Center' and x_pos_index == 2):
                pyautogui.press('left')
                x_pos_index -= 1
            elif (pos == 'Right' and x_pos_index != 2) or (pos == 'Center' and x_pos_index == 0):
                pyautogui.press('right')
                x_pos_index += 1

            # Vertical movement
            if MID_Y:
                posture = checkJumpCrouch(results, height, MID_Y)
                if posture == 'Jumping' and y_pos_index == 1:
                    pyautogui.press('up')
                    y_pos_index += 1
                elif posture == 'Crouching' and y_pos_index == 1:
                    pyautogui.press('down')
                    y_pos_index -= 1
                elif posture == 'Standing' and y_pos_index != 1:
                    y_pos_index = 1
        else:
            cv2.putText(frame, "JOIN BOTH HANDS TO START THE GAME", (5, height - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Check hands joined to start/resume
        if handsJoined(results, width, height):
            counter += 1
            if counter == num_of_frames:
                if not game_started and calibrated:
                    game_started = True
                    pyautogui.click(x=1300, y=800, button='left')
                    print("✅ Game started!")
                elif game_started:
                    pyautogui.press('space')
                    print("⏯ Game resumed!")
                counter = 0
        else:
            counter = 0

    # FPS
    time2 = time()
    if (time2 - time1) > 0:
        fps = 1.0 / (time2 - time1)
        cv2.putText(frame, f'FPS: {int(fps)}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
    time1 = time2

    cv2.imshow("Subway Surfers Pose Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Exiting game control mode.")
