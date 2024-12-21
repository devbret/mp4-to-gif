import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.gif')
            
            clip = VideoFileClip(input_path)
            
            clip.write_gif(output_path, fps=clip.fps, program='ffmpeg', opt='nq', fuzz=0)
            
            print(f"Converted {input_path} to {output_path}")

input_directory = "/path/to/your/video_files"
output_directory = "path/for/your/gifs"

convert_mp4_to_gif(input_directory, output_directory)

