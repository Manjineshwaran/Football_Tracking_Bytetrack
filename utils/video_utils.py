import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    for i in range(3):
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        cv2.imshow("Frame", frame)
        cv2.waitKey(300)
    cv2.destroyAllWindows()
    print("        ======frame======", frames[0])
    print("Number of frames: ", len(frames))
    return frames

def save_video(ouput_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 24
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0]))
    for frame in ouput_video_frames:
        out.write(frame)
    out.release()