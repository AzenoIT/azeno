from pydub import AudioSegment
from pydub.playback import play


def play_file(filename):
    ffmpeg_path = '/opt/homebrew/bin/ffmpeg'
    AudioSegment.ffmpeg = ffmpeg_path

    sound = AudioSegment.from_wav(filename)
    play(sound)
