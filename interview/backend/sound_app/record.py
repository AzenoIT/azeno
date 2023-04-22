import sounddevice as sd
import wavio
import numpy as np


def record(duration, fs, filename, threshold):
    print(f'Recording sound through {duration} seconds.')

    for i in range(duration):
        my_recording = sd.rec(int(fs), samplerate=fs, channels=1)
        sd.wait()

        rms_value = np.sqrt(np.mean(np.square(my_recording)))
        level = 20 * np.log10(rms_value / np.iinfo(np.int16).max)
        if level < threshold:
            print("Speak louder!")

        if i == 0:
            full_recording = my_recording
        else:
            full_recording = np.concatenate((full_recording, my_recording), axis=0)

    wavio.write(filename, full_recording, fs, sampwidth=2)
    print('Finished recording')
