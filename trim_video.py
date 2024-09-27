
import ffmpeg

#input_file = "/home/smartcity/PLUS/Muhammad/PycharmProjects/custom_dection _cup/parting_turn_over./output/Xpark_turnover_yolov8x_20240709_163550/parking_turn_over__20240709_163550.mp4"
input_file = r"D:\IDERIA\drive-download-20240501T051402Z-001\video_plus_baru\C21\C21-13.21.47-13.44.51.mp4"
output_file = r"D:\IDERIA\drive-download-20240501T051402Z-001\video_plus_baru\C21\C21-13.21.47-13.44.51_cut.mp4"
#output_file = "/home/smartcity/PLUS/Muhammad/drive-download-20240501T051402Z-001/C23_cut_1s.mp4"
start_time = "00:07:34"
end_time = "00:07:38"


ffmpeg.input(input_file, ss=start_time, to=end_time).output(output_file).run()


 