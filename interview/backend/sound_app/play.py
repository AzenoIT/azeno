from pydub import AudioSegment
from pydub.playback import play


def play_file(filename):
    sound = AudioSegment.from_wav(filename)
    play(sound)
