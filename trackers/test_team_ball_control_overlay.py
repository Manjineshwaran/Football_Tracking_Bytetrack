import cv2
import numpy as np

# Create a blank frame (e.g., 1280x720, 3 channels)
frame = np.ones((720, 1280, 3), dtype=np.uint8) * 200  # light gray background

# Simulate team ball control array (numpy array)
import numpy as np
team_ball_control = np.array([1]*30 + [2]*20 + [1]*10 + [2]*40)  # Example: 80 frames
frame_num = 79  # Last frame

# --- Overlay Drawing Logic ---
def draw_team_ball_control(frame, frame_num, team_ball_control):
    height, width = frame.shape[:2]
    rect_width = 500
    rect_height = 100
    pad_x = 20
    pad_y = 20
    x1 = width - rect_width - pad_x
    y1 = height - rect_height - pad_y
    x2 = width - pad_x
    y2 = height - pad_y

    overlay = frame.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), (255,255,255), -1)
    alpha = 0.4
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    team_ball_control_till_frame = team_ball_control[:frame_num+1]
    team_1_num_frames = (team_ball_control_till_frame==1).sum()
    team_2_num_frames = (team_ball_control_till_frame==2).sum()
    total = team_1_num_frames + team_2_num_frames
    team_1 = team_1_num_frames/total if total > 0 else 0
    team_2 = team_2_num_frames/total if total > 0 else 0

    text1 = f"Team 1 Ball Control: {team_1*100:.2f}%"
    text2 = f"Team 2 Ball Control: {team_2*100:.2f}%"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 3
    text_color = (255,255,255)
    outline_color = (0,0,0)
    text1_x = x1 + 20
    text1_y = y1 + 40
    text2_x = x1 + 20
    text2_y = y1 + 85
    cv2.putText(frame, text1, (text1_x, text1_y), font, font_scale, outline_color, thickness+2, cv2.LINE_AA)
    cv2.putText(frame, text2, (text2_x, text2_y), font, font_scale, outline_color, thickness+2, cv2.LINE_AA)
    cv2.putText(frame, text1, (text1_x, text1_y), font, font_scale, text_color, thickness, cv2.LINE_AA)
    cv2.putText(frame, text2, (text2_x, text2_y), font, font_scale, text_color, thickness, cv2.LINE_AA)
    return frame

# Draw overlay
frame_with_overlay = draw_team_ball_control(frame, frame_num, team_ball_control)

# Show result
cv2.imshow('Team Ball Control Overlay Test', frame_with_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows() 