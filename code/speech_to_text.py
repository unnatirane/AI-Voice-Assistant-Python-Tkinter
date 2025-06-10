

import speech_recognition as sr

import speech_recognition as sr
import speak


def speech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source) # methord
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        return voice_data

      except sr.UnknownValueError:
             speak.speak("sorry")
      except sr.RequestError:
            speak.speak('No internet connect please turn on you internet')

