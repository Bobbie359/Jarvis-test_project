import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # speech rate
# Set Bulgarian voice if available
for voice in engine.getProperty('voices'):
    if 'bg-BG' in voice.id or 'Daria' in voice.id:
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen(language="bg-BG"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            speak("I didn't understand you.")
            return None
        except sr.RequestError:
            speak("Internet connection problem.")
            return None
