import ffmpeg
import cv2

# Function to get video information using OpenCV
def get_video_info(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = total_frames / fps if fps > 0 else 0
    
    cap.release()
    
    return {
        "fps": fps,
        "total_frames": total_frames,
        "width": width,
        "height": height,
        "duration": duration
    }

# Function to print video information
def print_video_info(video_path, video_number):
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
video_path2 = '/home/muhammad/PLUS_new/home/smartcity/PLUS_new/Muhammad/drive-download-20240501T051402Z-001/video_plus_baru/C29/C26-12.48.20-13.11.22.mp4'
video_path1 = '/home/muhammad/PLUS_new/home/smartcity/PLUS_new/Muhammad/PycharmProjects/lisence_plate_tracking/output_ocr/C26-12.48.20-13.11.22_20240723_173159/C26-12.48.20-13.11.22_output_lowres.mp4'

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

# Video processing with FFmpeg
input_file = video_path2
output_file = "C26-12.48.20-13.11.22_converted.mp4"

# Use video 1 information for target width, height, and fps
target_width = info1['width']
target_height = info1['height']
target_fps = info1['fps']
video1_duration = info1['duration']
video2_duration = info2['duration']

try:
    # Set up the input
    input_stream = ffmpeg.input(input_file)
    
    # Calculate the speed factor to match Video 1's duration
    speed_factor = video1_duration / video2_duration

    # Apply video filters
    v = input_stream.video
    v = v.filter('scale', width=target_width, height=target_height)
    v = v.filter('setsar', sar='1/1')
    v = v.filter('fps', fps=target_fps)
    v = v.filter('setpts', f'{speed_factor}*PTS')

    # Set output parameters
    output = ffmpeg.output(v, output_file,
                           vcodec='libx264',
                           crf=23,
                           preset='medium',
                           an=None)  # 'an' flag to indicate no audio

    # Run the conversion
    ffmpeg.run(output, overwrite_output=True)
    
    print(f"Conversion complete. Output saved as {output_file}")

except ffmpeg.Error as e:
    print(f"FFmpeg error occurred: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
