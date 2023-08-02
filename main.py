import random
from gtts import gTTS
import os
import speech_recognition as sr
import pygame

def speak(text, language="ta"):
    tts = gTTS(text=text, lang=language, slow=False)
    temp_dir = os.environ.get("TEMP", "/tmp")  # Use /tmp as a fallback for non-Windows systems
    tts.save(os.path.join(temp_dir, "output.mp3"))

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pass

def listen(language="ta-IN"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("சொல்லுங்கள் (Speak now):")
        audio = recognizer.listen(mic)

    try:
        user_input = recognizer.recognize_google(audio, language=language)
        print(f"நீங்கள் சொன்ன சொற்கள்: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("நான் நீங்கள் சொல்லியதை அறியவில்லை (I couldn't understand what you said)")
    except sr.RequestError:
        print("Google செர்வருக்கு கேட்க முடியவில்லை (Couldn't request results from Google server)")

def tamil_jarvis():
    greetings = ["வணக்கம்", "வணக்கம் சகோ", "வணக்கம் அண்ணா", "வணக்கம் அக்கா"]
    responses = ["நலமாக இருக்கின்றேன்", "அன்பு நண்பா", "நீங்களுக்கு என்ன உதவி செய்ய முடியுமா?", "என்ன செய்ய வேண்டும்?"]

    greet = random.choice(greetings)
    response = random.choice(responses)

    speak(greet, language="ta")
    user_input = listen()

    if user_input:
        # Add more commands and responses here based on user_input
        if "உங்கள் பெயர் என்ன" in user_input:
            speak("என்னுடைய பெயர் கிளாரா", language="ta")

        elif "உனக்கு என்ன வயது" in user_input:
            speak(
                "என்னுடைய வயது ஐந்து", language="ta")

        elif "உன்னை உருவாக்கியது யார்" in user_input:
            speak(
                "என்னை உருவாக்கியது கென்னித் ராஜ்", language="ta")

        else:
            speak(response, language="ta")
    else:
        speak("நான் அனுமதி பெறவில்லை (I didn't get permission)", language="ta")

if __name__ == "__main__":
    tamil_jarvis()
