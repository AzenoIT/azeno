import pyttsx3
import io


def generate_speech(text, lang, gender):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)

    voice = get_voice(lang, gender)
    engine.setProperty('voice', voice['id'])

    output = io.BytesIO()
    engine.save_to_file(text, output)
    engine.runAndWait()
    return output.getvalue()
