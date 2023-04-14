import json

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def generate_json_with_voices(voices):
    voices_dict = {}
    for index, voice in enumerate(voices):
        voice_dict = {'name': voice.name, 'gender': voice.gender, 'languages': voice.languages}
        voices_dict[str(index)] = voice_dict

    with open('voices.json', 'w') as f:
        json.dump(voices_dict, f, indent=4)
