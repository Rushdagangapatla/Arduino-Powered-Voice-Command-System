'''what is ,who is,tell me about'''


import pyttsx3
import requests
import speech_recognition as sr

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set speech rate and voice (optional)
speaker.setProperty('rate', 130)  # Adjust the rate to your preference
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # Change index for different voices

# DuckDuckGo Instant Answer API URL
DUCKDUCKGO_URL = 'https://api.duckduckgo.com/'

# Initialize the recognizer for speech recognition
listener = sr.Recognizer()

def speak(text):
    """Function to speak out the given text."""
    speaker.say(text)
    speaker.runAndWait()

def truncate_text(text, word_limit=30):
    """Truncates5r the text to a specified number of words."""
    words = text.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    return text

def search_duckduckgo(query):
    """Searches DuckDuckGo for a given query and returns the abstract of the result."""
    try:
        params = {
            'q': query,
            'format': 'json',
            'no_redirect': '1',
            'no_html': '1',
            'skip_disambig': '1'
        }
        response = requests.get(DUCKDUCKGO_URL, params=params)
        data = response.json()
        
        if 'AbstractText' in data and data['AbstractText']:
            return truncate_text(data['AbstractText'])
        elif 'RelatedTopics' in data and data['RelatedTopics']:
            # Get the first related topic's text if available
            return truncate_text(data['RelatedTopics'][0]['Text'])
        else:
            return "Sorry, I couldn't find any relevant information."
    except Exception as e:
        print(f'An error occurred while searching: {e}')
        return "Sorry, I couldn't complete the search."

def listen_for_command():
    """Listens for voice input and returns it as text."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        return ''
    except Exception as e:
        print(f'An error occurred while listening: {e}')
        return ''

if __name__== '__main__':
    # Start with a prompt
    speak("Please tell me what you want to search.")
    query = listen_for_command()
    if query:
        print(f"Searching for: {query}")
        result = search_duckduckgo(query)
        print(result)
        speak(result)
    else:
        speak("Sorry, I didn't catch that. Please try again.")

