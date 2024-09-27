### 1. Prerequisites

Before running the scripts, make sure you have `ffmpeg` installed on your system.

#### Ubuntu
Install `ffmpeg` with:
```bash
sudo apt install ffmpeg
```

#### Windows
Follow the steps in this tutorial to install `ffmpeg`: [wikihow tutorial](https://www.wikihow.com/Install-FFmpeg-on-Windows).

Next, clone the repository and install the required packages:
```bash
git clone https://github.com/Muhdmechatronic/FFmpegToolbox-python.git
cd FFmpegToolbox-python
pip install -r requirements.txt
```

### 2. Tutorial for `convert_resolution.py`

#### Script Purpose
The `convert_resolution.py` script allows you to **lower the resolution** of a video. This is useful when you want to reduce file size or make the video compatible with lower-resolution devices. The script utilizes the `ffmpeg` library to scale down the resolution.

#### Resolutions Available for Downscaling
You should only **downscale** a video, meaning converting it to a lower resolution. Here are some common resolutions to convert from higher to lower:

| From Resolution (Higher) | To Resolution (Lower) |
|--------------------------|-----------------------|
| 3840x2160 (4K UHD)        | 1920x1080 (Full HD)   |
| 1920x1080 (Full HD)       | 1280x720 (HD)         |
| 1280x720 (HD)             | 854x480 (SD)          |
| 854x480 (SD)              | 640x360 (Low Res)     |

#### Code Explanation for `convert_resolution.py`

```python
import ffmpeg

def lower_resolution(input_file, output_file, width, height):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vf=f'scale={width}:{height}')
        .run()
    )

# Example usage
input_file = r"2103099-uhd_3840_2160_30fps.mp4"  # Your input video file
output_file = r"video3.mp4"  # Your output video file
width = 1280  # Desired width (you can change this)
height = 720  # Desired height (you can change this)

lower_resolution(input_file, output_file, width, height)
```

#### Key Points:
- **`input_file`**: This is the path to your input video. Replace `"2103099-uhd_3840_2160_30fps.mp4"` with your video file.
- **`output_file`**: This is the path where the lower-resolution video will be saved. Replace `"video3.mp4"` with your desired output file name.
- **`width` and `height`**: Specify the resolution you want to downscale to. In the example, it's set to **1280x720 (HD)**, but you can change it based on your requirements.

#### How It Works:
1. The function `lower_resolution()` uses the `ffmpeg` Python wrapper to process the video.
2. The `ffmpeg.input()` method takes the input video file.
3. The `.output()` method specifies the output file and the resolution (using the `scale` filter).
4. Finally, `.run()` executes the FFmpeg command to process the video.

### 3. Example Command to Convert from 1080p to 720p:
If you want to convert a video from **1080p (1920x1080)** to **720p (1280x720)**, modify the script like this:

```python
input_file = r"your_1080p_video.mp4"
output_file = r"output_720p.mp4"
width = 1280  # HD width
height = 720  # HD height

lower_resolution(input_file, output_file, width, height)
```

Running this script will downscale the video to 720p.

---

Let me know when you're ready for the next tutorial or if you need further clarifications!