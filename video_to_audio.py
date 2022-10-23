import os

from constants import VIDEO_DIR, AUDIO_DIR


def video_to_audio(file_name):
    print('------------ CONVERTING VIDEO TO AUDIO ------------')
    video_path = file_name
    video_name, video_extension = tuple(file_name.split('.'))

    # video_path = os.path.abspath(os.path.join(
    #         VIDEO_DIR, video_name)) + '.' + video_extension

    # audio_path = os.path.abspath(os.path.join(AUDIO_DIR, video_name))
    audio_path = video_name
    os.system(
        f'ffmpeg -i {video_path} -ar 16000 -ac 1 {audio_path}.wav -y')
    return video_name + '.wav'

# print(video_to_audio('videoplayback.mp4'))
# print("test")
