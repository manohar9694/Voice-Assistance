import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Set speaking rate

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for voice commands and convert them to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Could not connect to the speech recognition service.")
        return ""

def respond_to_command(command):
    """Handle basic voice commands."""
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif 'search for' in command:
        search_query = command.replace('search for', '').strip()
        speak(f"Searching for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'exit' in command or 'goodbye' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm sorry, I can only do basic tasks at the moment.")
    return True

def main():
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if command:
            if not respond_to_command(command):
                break

# Run the voice assistant
main()
























