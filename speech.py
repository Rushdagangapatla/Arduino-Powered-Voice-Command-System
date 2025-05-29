import pyttsx3
def speak(text):
    speaker=pyttsx3.init()
    speaker.setProperty('rate',150)
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
if __name__=="__main__":
    a="hello apsha"
    speak(a)
