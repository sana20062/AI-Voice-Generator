import torch
import soundfile as sf
import gradio as gr
from transformers import AutoProcessor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

processor = AutoProcessor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

def clone_voice(text, audio_path):
    inputs = processor(text=text, return_tensors="pt")

    speaker_embeddings = torch.randn(1, 512)

    speech = model.generate_speech(
        inputs["input_ids"],
        speaker_embeddings,
        vocoder=vocoder
    )

    sf.write("output.wav", speech.numpy(), 16000)

    return "output.wav"

demo = gr.Interface(
    fn=clone_voice,
    inputs=[
        gr.Textbox(label="Text"),
        gr.Audio(type="filepath", label="Upload Voice Sample")
    ],
    outputs="audio"
)

demo.launch()