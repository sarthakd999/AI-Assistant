# AI Voice-Activated Assistant with Feature Extensions

This Python project implements a voice-activated assistant capable of performing various tasks based on voice commands. The assistant leverages several libraries and APIs to provide functionalities such as web browsing, joke-telling, weather reporting, time telling, searching the web, and sending WhatsApp messages.

## Features

- **Voice Recognition**: Utilizes the `speech_recognition` library to recognize voice commands from the user.
- **Text-to-Speech**: Implements the `pyttsx3` library to convert text responses into spoken words.
- **Natural Language Processing (NLP)**: Utilizes the `spacy` library for natural language processing tasks, such as entity recognition and command analysis.
- **Web Browsing**: Allows the user to open a web browser and search the web for specific queries.
- **Joke-Telling**: Provides a selection of random jokes upon request.
- **Weather Reporting**: Retrieves and reports the current weather conditions for a specified location using the Weatherstack API.
- **Time Telling**: Reports the current time.
- **Wikipedia Facts**: Fetches and delivers concise facts about specified topics from Wikipedia.
- **Notepad and Calculator**: Opens Notepad or Calculator applications upon request.
- **WhatsApp Messaging**: Allows the user to send WhatsApp messages to predefined contacts.

## Usage

The user can interact with the assistant by speaking voice commands, triggering various actions based on the command's content. The assistant responds with spoken feedback or performs the requested tasks accordingly.

## Installation

To run the assistant, ensure you have the necessary libraries installed by running:

```bash
pip install speech_recognition spacy pyttsx3 pywhatkit
