# Audio Cutting Automation Script
from pydub import AudioSegment
import os

# path to the input audio file
input_audio_path = "Earth.mp3"
# load the audio file (use from_file for mp3 or other formats)
ext = os.path.splitext(input_audio_path)[1].lower().lstrip('.')
if ext == 'mp3':
	audio = AudioSegment.from_file(input_audio_path, format='mp3')
elif ext == 'wav':
	audio = AudioSegment.from_wav(input_audio_path)
else:
	audio = AudioSegment.from_file(input_audio_path)

# define start and end times in milliseconds
start_time = 10000  # 10 seconds
end_time = 20000    # 20 seconds
# cut the audio segment
cut_audio = audio[start_time:end_time]
# export the cut audio segment to a new file
output_audio_path = "cut_audio.wav"
cut_audio.export(output_audio_path, format="wav")
print(f"Cut audio segment saved to {output_audio_path}")