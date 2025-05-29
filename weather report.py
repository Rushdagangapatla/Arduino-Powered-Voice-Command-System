import pyttsx3
import requests
import speech_recognition as sr
speaker = pyttsx3.init() 
speaker.setProperty('rate', 130)  
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  
API_KEY = '3ec136d4c475adee4efe3c3219d70892'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
recognizer = sr.Recognizer()

def speak(text):
    """Function to speak out the given text."""
    speaker.say(text)
    speaker.runAndWait()

def get_weather(city):
    """Fetches the weather information for a given city."""
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if data['cod'] == 200:
            city_name = data['name']
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            report = f"The weather in {city_name} is currently {weather_desc} with a temperature of {temp} degrees Celsius."
            return report
        else:
            return "Sorry, I couldn't get the weather information for that location."
    except Exception as e:
        print(f'An error occurred while fetching weather information: {e}')
        return "Sorry, I couldn't get the weather information."

def listen_for_city():
    """Listen for the city name from the user."""
    with sr.Microphone() as source:
        print("Listening for city name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            city_name = recognizer.recognize_google(audio)
            print(f"City name received: {city_name}")
            return city_name
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the request.")
            speak("Sorry, there was a problem with the request.")
            return None

if __name__ == '__main__':
    speak("Please tell me the name of the city you want the weather for.")
    city = listen_for_city()
    
    if city:
        weather_report = get_weather(city)
        print(weather_report)
        speak(weather_report)
    else:
        speak("Unable to get the city name.")