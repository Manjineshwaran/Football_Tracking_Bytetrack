# import ultralytics
# model = ultralytics.YOLO("yolov8x.pt")

# print(model.names)




from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner

def main():
    # Read Video
    video_frames = read_video("D:/AI&DS/opencv/opencv_project/football_player_tracking_using_sv_byte_track/input_video/15sec_input_720p.mp4")
    # print(video_frames)

    # Initialize Tracker
    tracker = Tracker('D:/AI&DS/cv_job_assignment/stealth_mode/models/best.pt')
    
    # detections = tracker.get_object_tracks(video_frames)
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')

    print("\n =========tracks[ball]============ \n", tracks["ball"])
    # Interpolate Ball Positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
    
    print("\n =========tracks[ball]============ \n", tracks["ball"])
    # Save cropped image of a player from the first frame
    # for track_id, player in tracks['players'][0].items():
    #     bbox = player['bbox']  # [x1, y1, x2, y2]
    #     frame = video_frames[0]
    #     x1, y1, x2, y2 = map(int, bbox)
    #     cropped_image = frame[y1:y2, x1:x2]
    #     cv2.imwrite('output_videos/cropped_img.jpg', cropped_image)
    #     break

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['players'][0])

    print("\n =========team_assigner============ \n", team_assigner)
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    
     # Assign Ball Aquisition
    player_assigner =PlayerBallAssigner()
    team_ball_control= []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        print("\n =========player_assigner ball_bbox============ \n", ball_bbox)
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control= np.array(team_ball_control)

    # Draw output 
    ## Draw object Tracks
    print("\n =========final tracks========= \n", tracks)
    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)


    save_video(output_video_frames, "output_videos/output_video.mp4")

if __name__ == "__main__":
    main()

