# JarvisAI

Voice Assistant for macOS in Bulgarian

## Description
JarvisAI is a local voice assistant that works entirely in Bulgarian. It can execute commands such as opening a browser, writing an email, launching Discord, searching Google/YouTube, filling text, reporting time/date/holidays, and responds with Bulgarian speech. Activation is done via the wake word "Jarvis" using Porcupine.

## Main Features
- Bulgarian speech recognition and synthesis
- Wake word activation with Porcupine
- Local commands for macOS
- Easy startup via icon or login item
- Ready for sharing on GitHub (no API keys, with .gitignore and documentation)

## Installation
1. Clone the repository:
   ```
   git clone <your-repo-link>
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Add your OpenAI and Porcupine API keys in `config.py` and `wakeword_jarvis.py`.

## Usage
- Start the assistant via the script or desktop icon.
- Use the wake word "Jarvis" for activation.
- Give commands in Bulgarian.

## Configuration
- Add your API keys in `config.py` and `wakeword_jarvis.py`.
- You can change the device_index for the microphone according to your device.

## Sharing on GitHub
- Make sure all keys are removed from the code.
- The .gitignore file excludes sensitive and temporary files.
- You can share the project as a public repository.

## License
This project is open source and can be used freely for personal and educational purposes.
