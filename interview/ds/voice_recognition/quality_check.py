import os
from pydub import AudioSegment


class AudioSampler:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_volume(self):
        sound = AudioSegment.from_file(self.file_path)
        loudness = sound.dBFS

        if loudness < -12:
            print("We can't hear you, probably you are speaking too quiet")
        else:
            pass



