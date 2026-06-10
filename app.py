from TTS.api import TTS
import gradio as gr

print("Loading XTTS model...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def clone_voice(text, audio_file):
    output_file = "myvoice.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=audio_file,
        language="en",
        file_path=output_file
    )

    return output_file

demo = gr.Interface(
    fn=clone_voice,
    inputs=[
        gr.Textbox(
            label="Enter Text"
        ),
        gr.Audio(
            type="filepath",
            label="Upload Voice Sample"
        )
    ],
    outputs=gr.Audio(
        label="Generated Voice"
    ),
    title="AI Voice Cloning (XTTS)",
    description="Enter text and upload a voice sample."
)

demo.launch()