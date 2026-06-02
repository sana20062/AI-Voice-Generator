from TTS.api import TTS

tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

tts.tts_to_file(
    text="Hello, my name is Sana",
    file_path="output.wav"
)

print("Audio generated successfully!")