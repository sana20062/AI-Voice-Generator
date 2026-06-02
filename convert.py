from pydub import AudioSegment

audio = AudioSegment.from_file("samples/sana.m4a", format="m4a")
audio.export("samples/sana.wav", format="wav")

print("Conversion done!")