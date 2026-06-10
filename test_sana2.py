from TTS.api import TTS

print("Loading model...")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
    text="Hello everyone, this is a test of my new voice sample.",
    speaker_wav="samples/sana2.wav",
    language="en",
    file_path="test_output.wav"
)

print("Done!")