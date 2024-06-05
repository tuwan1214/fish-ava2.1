import cv2
# 读入视频文件
# cap = cv2.VideoCapture("F:/水产实验室摄像机/录像/2023-07-12/192.168.1.64_01_20230712182012676_6.mp4")
cap = cv2.VideoCapture("F:/Desktop/video-test.mp4")
# 获取总帧数
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# 按每3秒切割视频
time_interval = 6
fps = int(cap.get(cv2.CAP_PROP_FPS))
frames_per_interval = fps * time_interval
# 初始化帧编号
frame_index = 0
# 循环处理每一帧
while True:
    # 读取帧
    ret, frame = cap.read()
    if not ret:
        break
    # 如果当前帧编号是每一段的第一帧，则创建新的输出视频文件
    if frame_index % frames_per_interval == 0:
        # out_filename = "./7.12/14/"+"output_" + str(frame_index // frames_per_interval) + ".mp4"
        out_filename = "./video-test" + "output_" + str(frame_index // frames_per_interval) + ".mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(out_filename, fourcc, fps, (frame.shape[1], frame.shape[0]))
    # 将当前帧写入输出视频文件
    out.write(frame)
    # 更新帧编号
    frame_index += 1
# 释放视频文件
cap.release()
