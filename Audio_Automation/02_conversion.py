# Audio Conversion Script
from pydub import AudioSegment
import os
# path to the input audio file
AudioSegment.from_mp3("Earth.mp3")
input_audio_path = "Earth.mp3"
# load the audio file (use from_file for mp3 or other formats)
ext = os.path.splitext(input_audio_path)[1].lower().lstrip('.')
if ext == 'mp3':
    audio = AudioSegment.from_file(input_audio_path, format='mp3')
elif ext == 'wav':
    audio = AudioSegment.from_wav(input_audio_path)
else:
    audio = AudioSegment.from_file(input_audio_path)
# convert and export the audio file to a new format (e.g., mp3)
output_audio_path = "converted_audio.mp3"
audio.export(output_audio_path, format="mp3")
print(f"Converted audio file saved to {output_audio_path}")