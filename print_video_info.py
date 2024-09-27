import cv2

def get_video_info(video_path):
    """
    Get detailed information about a video file.
    """
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    
    # Get basic video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate duration
    duration = total_frames / fps if fps > 0 else 0
    
    # Release the video capture object
    cap.release()
    
    return {
        "fps": fps,
        "total_frames": total_frames,
        "width": width,
        "height": height,
        "duration": duration
    }

def print_video_info(video_path, video_number):
    """
    Print formatted video information.
    """
    info = get_video_info(video_path)
    if info:
        print(f"Video {video_number} Information:")
        print(f"  Path: {video_path}")
        print(f"  FPS: {info['fps']:.2f}")
        print(f"  Duration: {info['duration']:.2f} seconds")
        print(f"  Total Frames: {info['total_frames']}")
        print(f"  Frame Width: {info['width']} pixels")
        print(f"  Frame Height: {info['height']} pixels")
        print()

# Paths to the videos
video_path2 = '/home/muhammad/PLUS_new/home/smartcity/PLUS_new/Muhammad/drive-download-20240501T051402Z-001/video_plus_baru/C21/C21-13.21.47-13.44.51.mp4'
video_path1 = '/home/muhammad/PLUS_new/home/smartcity/PLUS_new/Muhammad/PycharmProjects/lisence_plate_tracking/output_ocr/C21-13.21.47-13.44.51_20240724_124352/C21-13.21.47-13.44.51_output_lowres.mp4'
# Print information for both videos
print_video_info(video_path1, 1)
print_video_info(video_path2, 2)

# Calculate and print the difference in duration
info1 = get_video_info(video_path1)
info2 = get_video_info(video_path2)

if info1 and info2:
    duration_diff = abs(info1['duration'] - info2['duration'])
    print(f"Duration Difference: {duration_diff:.2f} seconds")
    
    if duration_diff > 1:  # If the difference is more than 1 second
        print("Warning: The videos have significantly different durations.")
        print("This may cause synchronization issues when playing them together.")
    else:
        print("The videos have similar durations, which is good for synchronization.")