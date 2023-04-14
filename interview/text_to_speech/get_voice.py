import json

import pyttsx3


def get_voice(language, gender):
    with open('voices.json') as f:
        data = json.load(f)

    for voice in data['voices']:
        if voice['language'] == language and voice['gender'] == gender:
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.setProperty('voice', voice['id'])
            return engine

    return None
