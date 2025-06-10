import datetime
import speak
import webbrowser
import os


def Action(send):

    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak.speak("my name is virtual assistant")
        return "my name is virtual assistant"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn:
        speak.speak("hey ! how can i help you !")
        return "hey ! how can i help you !"

    elif "how are you" in data_btn:
        speak.speak("i am doing great")
        return "i am doing great"

    elif "thank You" in data_btn or " thanks" in data_btn:
        speak.speak("its my pleasure to stay with you")
        return "its my pleasure to stay with you"

    elif "good morning" in data_btn:
        speak.speak("good Morning, i think you might need some help")
        return "good morning, i think you might need some help"

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " Hour : ", (str)(current_time.minute) + " Minute"
        speak.speak(Time)
        return str(Time)

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok ")
        return "ok sir"
    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        speak.speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open")
        return "YouTube open"

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..."

    else:
        speak.speak("i'm able to understand!")
        return "i'm able to understand!"