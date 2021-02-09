import cv2
import os

def save_frame_range_sec(video_path, start_sec, stop_sec, step_sec,
                         dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    fps = cap.get(cv2.CAP_PROP_FPS)
    fps_inv = 1 / fps

    sec = start_sec
    page = 0
    while sec < stop_sec:
        n = round(fps * sec)
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(
                '{}_{}_{:.2f}.{}'.format(
                    base_path, page, n * fps_inv, ext
                ),
                frame
            )
            page += 1
        else:
            return
        sec += step_sec

v_path = 'data/video2.mp4'
d_path = 'data/result0'
b_name = 'p'

save_frame_range_sec(v_path, 0.5, 40, 1, d_path, b_name)

'''
https://gammasoft.jp/blog/python-string-format/
https://note.nkmk.me/python-opencv-videocapture-file-camera/
https://note.nkmk.me/python-opencv-video-to-still-image/
https://qiita.com/shinfrom/items/b8f2aec43638516cfd0d
'''