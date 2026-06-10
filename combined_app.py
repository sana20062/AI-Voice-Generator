from TTS.api import TTS
import gradio as gr
import subprocess
import shutil
import os

VOICE_PROJECT = r"C:\Users\user\OneDrive\Desktop\Voice clone project"
SADTALKER_PATH = r"C:\Users\user\Desktop\SadTalker"

SADTALKER_PYTHON = r"C:\Users\user\Desktop\SadTalker\sadtalker_env\Scripts\python.exe"

print("Loading XTTS model...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")


def generate_video(text, voice_sample, image_file):

    # Generate cloned voice
    output_audio = os.path.join(VOICE_PROJECT, "myvoice.wav")

    tts.tts_to_file(
        text=text,
        speaker_wav=voice_sample,
        language="en",
        file_path=output_audio
    )

    # Copy audio to SadTalker
    shutil.copy(
        output_audio,
        os.path.join(
            SADTALKER_PATH,
            "examples",
            "driven_audio",
            "myvoice.wav"
        )
    )

    # Copy image to SadTalker
    shutil.copy(
        image_file,
        os.path.join(
            SADTALKER_PATH,
            "examples",
            "source_image",
            "input.jpg"
        )
    )

    cmd = [
        SADTALKER_PYTHON,
        "inference.py",
        "--driven_audio",
        "examples\\driven_audio\\myvoice.wav",
        "--source_image",
        "examples\\source_image\\input.jpg",
        "--result_dir",
        "results"
    ]

    print("Running SadTalker...")

    env = os.environ.copy()

    env["PATH"] += os.pathsep + r"C:\Users\user\Downloads\ffmpeg-8.1.1-essentials_build (1)\ffmpeg-8.1.1-essentials_build\bin"
    print("FFMPEG PATH:", env["PATH"])

    subprocess.run(
        cmd,
        cwd=SADTALKER_PATH,
        env=env
    )

    # Find newest results folder
    results_dir = os.path.join(
        SADTALKER_PATH,
        "results"
    )

    mp4_files = [
        os.path.join(results_dir, f)
        for f in os.listdir(results_dir)
        if f.endswith(".mp4")
    ]

    latest_video = max(
        mp4_files,
        key=os.path.getmtime
    )

    gradio_video = os.path.join(
        VOICE_PROJECT,
        "output_video.mp4"
    )

    shutil.copy(
        latest_video,
        gradio_video
    )

    print("Returning:", gradio_video)

    return gradio_video

demo = gr.Interface(
    fn=generate_video,
    inputs=[
        gr.Textbox(label="Enter Text"),
        gr.Audio(
            type="filepath",
            label="Voice Sample"
        ),
        gr.Image(
            type="filepath",
            label="Face Image"
        )
    ],
    outputs=gr.Video(
        label="Generated Talking Video"
    ),
    title="XTTS + SadTalker AI Avatar"
)

demo.launch()