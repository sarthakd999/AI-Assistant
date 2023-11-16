import speech_recognition as sr
import requests
import spacy
import webbrowser
import pyttsx3
import random
import datetime
import wikipedia
import os
import subprocess
from datetime import datetime
import pywhatkit

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize spaCy NLP
nlp = spacy.load("en_core_web_sm")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set the name of the assistant
assistant_name = "Lily"  # Change this to the desired name

# Set the properties for a female voice
engine.setProperty("rate", 150)  # Adjust the speed as needed
# voices = engine.getProperty("voices")

# Set the voice to Zira
zira_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("voice", zira_voice_id)

# Function to perform actions based on commands
def perform_action(command):
    if "open browser" in command:
        speak("Opening the web browser.")
        webbrowser.open("http://www.google.com")
    
    elif "search the web for" in command:
        search_query = command.replace("search the web for", "")
        speak(f"Searching the web for {search_query}.")
        webbrowser.open(f"http://www.google.com/search?q={search_query}")
    
    elif "tell me a joke" in command:
        joke = random.choice(["Why don't scientists trust atoms? Because they make up everything!", "Why did the computer go to therapy? It had too many bytes of emotional baggage!"])
        speak(joke)
    
    elif "tell me the weather" in command:
        get_weather()

    elif "tell me the time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    
    elif "tell me a fact about" in command:
        entity = command.replace("tell me a fact about", "").strip()
        try:
            summary = wikipedia.summary(entity, sentences=1)
            speak(f"Here is a fact about {entity}: {summary}")
        except wikipedia.exceptions.WikipediaException:
            speak(f"Sorry, I couldn't find information about {entity}.")
    
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
    
    elif "open calculator" in command:
        speak("Opening Calculator.")
        subprocess.Popen("calc.exe")
    
    elif "send whatsapp message" in command:
        speak("Please tell me the person's name")
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
            
            command = recognizer.recognize_google(audio)
            print("Recognized command:", command)
            
            contact_name = command.lower()
       
            send_whatsapp_msg(contact_name)

    else:
        speak(f"Sorry, {assistant_name} didn't understand that command.")

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for sending whatsapp msg
def send_whatsapp_msg(contact_name):

    # Create a dictionary to map names to phone numbers
    contact_mapping = {
        'sis': '+918767085782',
        'dad': '+919869701186',
        'mom': '+919869611505',
        'omkar': '+919920465918',
        'omkar yadav': '+919930521118',
        'mansi': '+918382999723',
        'saamba': '+87123456'
        # Add more contacts as needed
    }

    # Get the current date and time
    current_datetime = datetime.now()

    # Extract hours and minutes
    c_hr = current_datetime.hour
    c_min = current_datetime.minute
    
    # Get the phone number associated with the contact name
    contact_number = contact_mapping.get(contact_name)

    if contact_number:
        # Sending the message with adjusted timing parameters
        pywhatkit.sendwhatmsg(contact_number,"Hi this is a test message",
                            c_hr, c_min + 2)
    else:
        print(f"Contact '{contact_name}' not found.")

#fuction to get weather
def get_weather():
    base_url = "http://api.weatherstack.com/current"
    city = "Mumbai"
    params = {
        "access_key": "3dcc91c9d66d5e0132b56905c88d6081",
        "query": "Mumbai",
        "units": "m"  # Use "f" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["current"]["temperature"]
        description = weather_data["current"]["weather_descriptions"][0]

        speak(f"Temperature in {city} is"+ str(temperature) + "°C")
        print("Description:", description)
        
    else:
        print("Error:", response.status_code)
        


# Function to get voice command
def get_voice_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Main loop
while True:
    voice_command = get_voice_command()

    if voice_command:
        analyze_text = nlp(voice_command)
        perform_action(voice_command)
