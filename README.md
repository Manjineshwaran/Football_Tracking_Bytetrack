# Football Player Tracking Using SV ByteTrack

## Overview
This project tracks football players and the ball in a video using object detection and tracking, assigns teams based on jersey color, and determines which player and team has ball possession over time. The output is an annotated video visualizing these results.

## Features
- Detects and tracks players, referees, and the ball in football match videos
- Assigns players to teams based on jersey color clustering
- Identifies which player has the ball in each frame
- Visualizes team ball control statistics over time
- Outputs an annotated video with overlays

## Requirements
- Python 3.8+
- [Ultralytics YOLOv8](https://docs.ultralytics.com/) (for object detection)
- OpenCV (`cv2`)
- NumPy
- scikit-learn
- pandas
- [supervision](https://github.com/roboflow/supervision) (for ByteTrack)

Install dependencies with:
```bash
pip install ultralytics opencv-python numpy scikit-learn pandas supervision
```

## File Structure
- `main.py` — Main entry point, runs the full pipeline
- `trackers/` — Tracking logic (ByteTrack, drawing, interpolation)
- `team_assigner/` — Team color clustering and assignment
- `player_ball_assigner/` — Assigns ball possession to players
- `utils/` — Video I/O and bounding box utilities
- `output_videos/` — Output and intermediate video/images
- `runs/` — Example detection outputs
- `stubs/` — (Optional) Pickled tracking results for faster reruns

## How It Works: Step-by-Step

### 1. Read the Input Video
- The video is loaded frame-by-frame using `read_video` from `utils/video_utils.py`.
- Only the first 100 frames are read by default (can be adjusted in code).

### 2. Object Detection and Tracking
- The `Tracker` class (in `trackers/tracker.py`) loads a YOLOv8 model and a ByteTrack tracker.
- For each frame (or batch), YOLO detects players, referees, and the ball.
- ByteTrack assigns consistent IDs to each detected object across frames.
- Optionally, tracking results can be loaded from a stub file for speed.
- Ball positions are interpolated to fill in missing detections.

### 3. Team Assignment
- The `TeamAssigner` class (in `team_assigner/team_assigner.py`) clusters player jersey colors using KMeans.
- For each player, the dominant color of the upper jersey is extracted.
- Players are grouped into two teams based on color similarity.
- Each player is assigned a team and a representative color for visualization.

### 4. Ball Possession Assignment
- The `PlayerBallAssigner` class (in `player_ball_assigner/player_ball_assigner.py`) determines which player is closest to the ball in each frame.
- If a player is within a threshold distance to the ball, they are marked as having possession.
- The team of the player with the ball is recorded for each frame.

### 5. Visualization and Output
- The tracker draws bounding ellipses for players and referees, triangles for the ball, and overlays team colors and IDs.
- Ball possession is visualized with a triangle on the player and a team control bar overlay.
- The annotated frames are saved as a new video using `save_video`.

## Running the Project
1. Place your input video at the path specified in `main.py` (default is an absolute path; update as needed).
2. Place your YOLOv8 model weights at the path specified in `main.py`.
3. Run the main script:
   ```bash
   python main.py
   ```
4. The output video will be saved to `output_videos/output_video.mp4`.

## Customization
- To process more frames, change the loop in `read_video`.
- To use your own model or video, update the paths in `main.py`.
- To adjust ball possession sensitivity, change `max_player_ball_distance` in `PlayerBallAssigner`.

## Notes
- The code uses OpenCV's GUI functions (`cv2.imshow`). If running on a headless server, comment out or remove these lines.
- The project expects a specific YOLOv8 model trained to detect players, referees, and the ball.
- For reproducibility or debugging, you can use the stub system to cache tracking results.

## Credits
- YOLOv8 by Ultralytics
- ByteTrack and Supervision by Roboflow
- KMeans clustering from scikit-learn

---

For questions or improvements, please open an issue or pull request. 