import ffmpeg

input_file = "/home/smartcity/PLUS/Muhammad/drive-download-20240501T051402Z-001/video_plus_baru/OneDrive_2_7-12-2024/C29/C26-13.57.30-14.20.34.mp4"  # 
output_file = "/home/smartcity/PLUS/Muhammad/drive-download-20240501T051402Z-001/video_plus_baru/OneDrive_2_7-12-2024/C26-13.57.30-14.20.34.mp4"  # 
ffmpeg.input(input_file).output(output_file).run()