from moviepy.editor import AudioFileClip

def convert_to_wav(input_path, output_path="processed_audio.wav"):
    clip = AudioFileClip(input_path)
    clip.write_audiofile(output_path, fps=16000, nbytes=2, codec='pcm_s16le')
    clip.close()
    return output_path
  
