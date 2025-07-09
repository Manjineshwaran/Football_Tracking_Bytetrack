# n={
#     "player":[],
#     "refree":[]
# }
# print("\n n = ", n)
# print("\n n[player] = ",n["player"])

# n["player"].append({})
# n["refree"].append({})

# print("\n n = ", n)
# print("\n n[player] = ",n["player"])

# for i in range(2):
#     n["player"][0][i] = {"bbox":[1,2,3,4]}

# print("\n n = ", n)
# print("\n n[player] = ",n["player"])


import cv2

# Input and output file paths
input_video_path = "D:/AI&DS/cv_job_assignment/stealth_mode/Assignment Materials/15sec_input_720p.mp4"  # Change this to your 15s video path
output_video_path = 'output_1s.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate number of frames for 1 second
frames_to_save = int(fps * 1)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

frame_count = 0
while frame_count < frames_to_save:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    frame_count += 1

cap.release()
out.release()
print(f"Saved first 1 second to {output_video_path}")