from TTS.api import TTS
import subprocess
import os

print("Loading XTTS...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

text = "Hello, this is a test."
voice_sample = "samples/sana2.wav"

output_audio = "myvoice.wav"

tts.tts_to_file(
    text=text,
    speaker_wav=voice_sample,
    language="en",
    file_path=output_audio
)

print("Audio generated")

sadtalker_path = r"C:\Users\user\Desktop\SadTalker"
import shutil

shutil.copy(
    output_audio,
    os.path.join(
        sadtalker_path,
        "examples",
        "driven_audio",
        "myvoice.wav"
    )
)

cmd = [
    r"C:\Users\user\Desktop\SadTalker\sadtalker_env\Scripts\python.exe",
    "inference.py",
    "--driven_audio",
"examples\\driven_audio\\myvoice.wav",
    "--source_image",
    "examples\\source_image\\srk.jfif",
    "--result_dir",
    "results"
]

print("Starting SadTalker...")

subprocess.run(
    cmd,
    cwd=sadtalker_path
)

print("Done!")