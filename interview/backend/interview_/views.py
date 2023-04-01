import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render
import webbrowser


def speech_recognition_template(request):
    return render(request, 'interview_/speech_recognition.html')


# Ten shit niestety mi nie działa, a powinien... Sypie błędem braku pyaudio. Może u Was zadziała?

def speech_recognition_view(request):
    # create an instance of the Recognizer class
    r = sr.Recognizer()

    # use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        webbrowser.open('https://www.google.com/search?q=enable+microphone+in+browser')
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        # print("Google Speech Recognition thinks you said: " + text)
    except sr.UnknownValueError:
        # print("Google Speech Recognition could not understand audio")
        text = 'Google Speech Recognition could not understand audio'
    except sr.RequestError as e:
        # print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = 'Could not request results from Google Speech Recognition service'

    # return the recognized text as a JSON response
    return JsonResponse({'text': text})
