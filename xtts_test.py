from TTS.api import TTS

print("Loading XTTS model...")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
text="Hello everyone, I am Pratistha and this is my AI voice cloning project.",
speaker_wav="samples/sana1.wav",
language="en",
file_path="cloned_output.wav"
)

print("Done! Audio saved as cloned_output.wav")
