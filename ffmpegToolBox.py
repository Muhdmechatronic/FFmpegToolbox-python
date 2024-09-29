import cv2
import ffmpeg
import os

class VideoProcessor:
    def __init__(self, input_file, output_file=None):
        """
        Initialize the processor. If output_file is not provided, it will use the input file's name
        and extension by default.
        """
        self.input_file = input_file
        self.output_file = output_file or self._generate_output_file(input_file)

    def _generate_output_file(self, input_file):
        """
        Generates the default output file name based on the input file.
        """
        base_name, ext = os.path.splitext(input_file)
        return f"{base_name}_converted{ext}"

    def get_video_info(self, video_path):
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
        
        cap.release()
        return {
            "fps": fps,
            "total_frames": total_frames,
            "width": width,
            "height": height,
            "duration": duration
        }

    def print_video_info(self, video_number='Original'):
        """
        Print formatted video information for the input video.
        """
        info = self.get_video_info(self.input_file)
        if info:
            print(f"Video {video_number} Information:")
            print(f"  Path: {self.input_file}")
            print(f"  FPS: {info['fps']:.2f}")
            print(f"  Duration: {info['duration']:.2f} seconds")
            print(f"  Total Frames: {info['total_frames']}")
            print(f"  Resolution: {info['width']}x{info['height']}")
            print()
        return info

    def print_converted_video_info(self):
        """
        Print information for the converted video.
        """
        info = self.get_video_info(self.output_file)
        if info:
            print(f"Converted Video Information:")
            print(f"  Path: {self.output_file}")
            print(f"  FPS: {info['fps']:.2f}")
            print(f"  Duration: {info['duration']:.2f} seconds")
            print(f"  Total Frames: {info['total_frames']}")
            print(f"  Resolution: {info['width']}x{info['height']}")
            print()
        return info

    def convert_resolution(self, max_dimension=None):
        """
        Convert the resolution of the video to the specified maximum width or height, while maintaining aspect ratio.
        """
        video_info = self.get_video_info(self.input_file)
        if not video_info:
            return

        original_width = video_info['width']
        original_height = video_info['height']
        
        # Check if width or height is provided, calculate the other while maintaining aspect ratio
        if max_dimension:
            aspect_ratio = original_width / original_height
            if original_width >= original_height:
                # Scale down by width
                new_width = max_dimension
                new_height = int(new_width / aspect_ratio)
            else:
                # Scale down by height
                new_height = max_dimension
                new_width = int(new_height * aspect_ratio)
        else:
            # If no dimension is provided, use original dimensions
            new_width = original_width
            new_height = original_height

        # Use FFmpeg to convert the video while maintaining the aspect ratio
        ffmpeg.input(self.input_file).output(self.output_file, vf=f'scale={new_width}:{new_height}').run()

        print(f"Video resolution converted to {new_width}x{new_height} and saved as {self.output_file}")

    def convert_fps(self, fps):
        """
        Convert the frame rate (FPS) of the video.
        """
        ffmpeg.input(self.input_file).output(self.output_file, r=fps).run()
        print(f"Video FPS converted to {fps} and saved as {self.output_file}")

    def trim_video(self, start_time, end_time):
        """
        Trim the video between start_time and end_time.
        """
        ffmpeg.input(self.input_file, ss=start_time, to=end_time).output(self.output_file).run()
        print(f"Video trimmed from {start_time} to {end_time} and saved as {self.output_file}")

    def convert_all(self, max_dimension=None, fps=None, start_time=None, end_time=None):
        """
        Perform all conversions (resolution, FPS, and trimming) as needed.
        """
        output = ffmpeg.input(self.input_file)
        video_info = self.get_video_info(self.input_file)
        if not video_info:
            return

        original_width = video_info['width']
        original_height = video_info['height']
        
        # Check if width or height is provided, calculate the other while maintaining aspect ratio
        if max_dimension:
            aspect_ratio = original_width / original_height
            if original_width >= original_height:
                # Scale down by width
                new_width = max_dimension
                new_height = int(new_width / aspect_ratio)
            else:
                # Scale down by height
                new_height = max_dimension
                new_width = int(new_height * aspect_ratio)
        else:
            # If no dimension is provided, use original dimensions
            new_width = original_width
            new_height = original_height

        # Apply the resolution scaling
        output = output.filter('scale', new_width, new_height)
        print(f"Converting resolution to {new_width}x{new_height}...")
        
        # Apply the FPS filter before output
        if fps:
            print(f"Converting FPS to {fps}...")
            output = output.filter('fps', fps=fps)

        # Apply the trimming if both start_time and end_time are provided
        if start_time and end_time:
            output = output.trim(start=start_time, end=end_time).setpts('PTS-STARTPTS')
            print(f"Trimming video from {start_time} to {end_time}...")

        # Output the video to the specified file
        output = output.output(self.output_file)
        output.run()
        print(f"All operations completed and saved as {self.output_file}")

    def convert_to_match_video(self, video_to_match):
        """
        Convert the input video (self.input_file) to match the FPS, resolution, and duration of another video (video_to_match).
        """
        info_to_match = self.get_video_info(video_to_match)
        info_input = self.get_video_info(self.input_file)

        if not info_to_match or not info_input:
            print("Error: Could not retrieve video information.")
            return

        target_width = info_to_match['width']
        target_height = info_to_match['height']
        target_fps = info_to_match['fps']
        duration_to_match = info_to_match['duration']
        duration_input = info_input['duration']

        # Calculate speed factor to adjust the duration of the video to match
        speed_factor = duration_to_match / duration_input if duration_input > 0 else 1.0

        # Apply the transformations
        input_stream = ffmpeg.input(self.input_file)
        v = input_stream.video.filter('scale', target_width, target_height).filter('fps', fps=target_fps)
        v = v.filter('setpts', f'{speed_factor}*PTS')

        # Save the output
        output = ffmpeg.output(v, self.output_file, vcodec='libx264', crf=23, preset='medium')
        output.run(overwrite_output=True)

        print(f"Converted video to match FPS: {target_fps}, Resolution: {target_width}x{target_height}, and Duration: {duration_to_match}.")

    def convert_video_format(self, target_format):
        """
        Convert the video format (e.g., MP4 to MKV or any other format).
        """
        # Generate a new output file with the target format's extension
        base_name, _ = os.path.splitext(self.input_file)
        converted_file = f"{base_name}_converted.{target_format}"
        
        # Use FFmpeg to convert the video format
        ffmpeg.input(self.input_file).output(converted_file).run(overwrite_output=True)
        
        print(f"Video format converted to {target_format} and saved as {converted_file}")
        self.output_file=converted_file
        return converted_file

# Example Usage

# Example Usage

input_file = r"D:\IDERIA\PycharmProjects\ConvertVideo\ConvertVideo\C21-13.21.47-13.44.51_trim.mp4"
output_file = r"D:\IDERIA\PycharmProjects\ConvertVideo\ConvertVideo\C26-12.48.20-13.11.22_.mp4"
video_to_match = r"D:\IDERIA\PycharmProjects\lisence_plate_tracking\output_ocr\C26-12.48.20-13.11.22_20240723_173159\C26-12.48.20-13.11.22_output_lowres.mp4"
# Initialize the video processor
processor = VideoProcessor(input_file, output_file)

# Print video information
processor.print_video_info()

# Convert FPS
processor.convert_fps(5)  # Example: convert to 30 FPS

# Trim video
#processor.trim_video("00:07:34", "00:07:38")  # Example: trim video between times\

# Convert to match video 1 properties (FPS, resolution, duration)
#processor.convert_to_match_video(video_to_match)

# Convert resolution, FPS, and trim video in one go
#processor.convert_all(max_dimension=720, fps=5, start_time="00:07:34", end_time="00:07:38")

# Convert smaller resolution 
#processor.convert_resolution(max_dimension=720)

# Convert the video format to MKV
#processor.convert_video_format("mkv")

processor.print_converted_video_info()