import pyttsx3
def speak(text):
    bot = pyttsx3.init() #initialize
    rate = bot.getProperty('rate')
    bot.setProperty('rate', rate-70)
    bot.say(text)
    bot.runAndWait()