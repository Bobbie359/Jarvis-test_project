#Need to add API 
import openai
from config import OPENAI_API_KEY, LANGUAGE
from voice import speak, listen
from personality import system_prompt
from commands import execute_command

openai.api_key = OPENAI_API_KEY

def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": message}
        ]
    )
    return response["choices"][0]["message"]["content"]

def main():
    speak("Hello. I am Jarvis. I'm listening.")
    while True:
        query = listen(language=LANGUAGE)
        if not query:
            continue

        response = execute_command(query)
        if response:
            speak(response)
            if "turn off" in query.lower():
                break
        else:
            gpt_response = ask_gpt(query)
            speak(gpt_response)

if __name__ == "__main__":
    main()
