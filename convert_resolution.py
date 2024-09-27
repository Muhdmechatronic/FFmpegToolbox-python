import ffmpeg

def lower_resolution(input_file, output_file, width, height):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vf=f'scale={width}:{height}')
        .run()
    )

# Example usage
input_file = r"2103099-uhd_3840_2160_30fps.mp4"
output_file = r"video3.mp4"
width = 1280  # Desired width
height = 720  # Desired height

lower_resolution(input_file, output_file, width, height)
