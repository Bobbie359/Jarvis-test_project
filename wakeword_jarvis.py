import pvporcupine
import pyaudio
import struct
import subprocess
import time

# Use the built-in laptop microphone (device_index = 2)
device_index = 2

# Wake word for Porcupine ("jarvis")
# IMPORTANT: Add your Porcupine access_key here!
access_key = ""
porcupine = pvporcupine.create(
    access_key=access_key,
    keywords=["jarvis"]
)
pa = pyaudio.PyAudio()
stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    input_device_index=device_index,
    frames_per_buffer=porcupine.frame_length
)

print(f"Listening for 'Jarvis'... (microphone: {device_index})")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)
        if result >= 0:
            print("\nDetected: Jarvis!")
            subprocess.Popen([
                "/Users/borislavignatov/Downloads/JarvisAI/.venv/bin/python",
                "/Users/borislavignatov/Downloads/JarvisAI/main.py"
            ])
            time.sleep(2)
finally:
    try:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
    except Exception as e:
        print(f"Error closing resources: {e}")
