# VideoProcessor

## Overview

The `VideoProcessor` class is a Python utility for processing videos using `OpenCV` and `FFmpeg`. It allows users to manipulate video files by changing their resolution, frame rate, duration, and format. The class provides an easy-to-use interface for performing common video processing tasks, making it suitable for developers and researchers working with multimedia data.

## Prerequisites

Before running the scripts, ensure you have `ffmpeg` installed on your system.

### Ubuntu

Install `ffmpeg` with the following command:

```bash
    sudo apt install ffmpeg
```

### Windows

Follow the steps in this tutorial to install `ffmpeg`: [Install FFmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows).

Next, clone the repository and install the required packages:

```bash
    git clone https://github.com/Muhdmechatronic/FFmpegToolbox-python.git
    cd FFmpegToolbox-python
    pip install -r requirements.txt
```
## Usage

### Initializing the Video Processor

To use the `VideoProcessor`, first initialize it with an input video file. You can also specify an output file name; if not provided, a default name will be generated.

```python
from video_processor import VideoProcessor

input_file = r"D:\path\to\your\input_video.mp4"
output_file = r"D:\path\to\your\output_video.mp4"
processor = VideoProcessor(input_file, output_file)
```

### Example Methods

1. **Print Video Information**

   You can retrieve and print detailed information about the input video:

   ```python
   processor.print_video_info()
   ```

2. **Convert Frame Rate**

   To convert the video to a specific frame rate:

   ```python
   processor.convert_fps(30)  # Converts the video to 30 FPS
   ```

3. **Trim Video**

   To trim the video between specified start and end times:

   ```python
   processor.trim_video("00:01:00", "00:02:00")  # Trims the video from 1:00 to 2:00
   ```

4. **Convert to Match Another Video**

   To adjust the input video to match the properties (FPS, resolution, duration) of another video:

   ```python
   video_to_match = r"D:\path\to\your\reference_video.mp4"
   processor.convert_to_match_video(video_to_match)
   ```

5. **Convert Resolution**

   To change the resolution while maintaining the aspect ratio:

   ```python
   processor.convert_resolution(max_dimension=720)  # Downscale to max 720 pixels
   ```

6. **Convert Video Format**

   To convert the video to a different format (e.g., MP4 to MKV):

   ```python
   processor.convert_video_format("mkv")
   ```

7. **Print Converted Video Information**

   Finally, print information about the converted video:

   ```python
   processor.print_converted_video_info()
   ```

### Resolutions Available for Downscaling

You should only **downscale** a video. Below are common resolutions for converting from higher to lower:

| From Resolution (Higher) | To Resolution (Lower) |
|--------------------------|-----------------------|
| 3840x2160 (4K UHD)      | 1920x1080 (Full HD)   |
| 1920x1080 (Full HD)     | 1280x720 (HD)         |
| 1280x720 (HD)           | 854x480 (SD)          |
| 854x480 (SD)            | 640x360 (Low Res)     |

### Supported File Formats

FFmpeg can convert between a wide range of file formats. Below is a list of popular formats you can use for video and audio conversion.

#### **Video Formats**:
- **MP4**: `.mp4`
- **MKV**: `.mkv`
- **AVI**: `.avi`
- **MOV**: `.mov`
- **WMV**: `.wmv`
- **FLV**: `.flv`
- **WEBM**: `.webm`
- **MPEG**: `.mpeg` or `.mpg`
- **OGV**: `.ogv`
- **TS**: `.ts`

#### **Audio Formats**:
- **MP3**: `.mp3`
- **AAC**: `.aac`
- **WAV**: `.wav`
- **OGG**: `.ogg`
- **FLAC**: `.flac`
- **WMA**: `.wma`

#### **Other Multimedia Formats**:
- **GIF**: Convert videos to animated `.gif` files.
- **MP3 Extraction**: Convert video files (like `.mp4`, `.mkv`) to audio formats like `.mp3`.

## Conclusion

The `VideoProcessor` class provides a powerful yet user-friendly interface for common video processing tasks. Whether you need to change the resolution, frame rate, duration, or format of your videos, this tool has you covered.

For further questions or contributions, feel free to reach out or submit a pull request.


### Explanation of the Structure
1. **Overview**: Introduces the class and its purpose.
2. **Prerequisites**: Lists the requirements for running the script.
3. **Usage**: Provides a step-by-step guide on how to use the class, including initialization and examples of method usage.
4. **Resolutions Available for Downscaling**: Offers a table of common resolutions for reference.
5. **Supported File Formats**: Lists video and audio formats supported by FFmpeg for conversion.
6. **Conclusion**: Encourages users to reach out with questions or contributions.

Feel free to modify any section or add additional details specific to your project!