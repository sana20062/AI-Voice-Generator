import torch
import soundfile as sf
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

print("Loading XTTS (offline mode)...")

model_path = "xtts_model"

config = XttsConfig()
config.load_json(f"{model_path}/config.json")

model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir=model_path, eval=True)

print("Cloning voice...")

wav = model.synthesize(
    text="I am testing my real voice cloning system",
    speaker_wav="samples/sana.wav",
    language="en"
)

sf.write("output.wav", wav["wav"], 22050)

print("DONE → output.wav created")