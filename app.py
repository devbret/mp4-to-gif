import os
import logging
from moviepy.editor import VideoFileClip

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conversion.log"),
        logging.StreamHandler()
    ]
)

def convert_mp4_to_gif(input_directory, output_directory):
    if not os.path.exists(input_directory):
        logging.error(f"Input directory does not exist: {input_directory}")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        logging.info(f"Created output directory: {output_directory}")

    for filename in os.listdir(input_directory):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.gif')
            
            try:
                logging.info(f"Processing file: {input_path}")

                clip = VideoFileClip(input_path)

                clip.write_gif(output_path, fps=clip.fps, program='ffmpeg', opt='nq', fuzz=0)
                
                logging.info(f"Successfully converted {input_path} to {output_path}")
            except Exception as e:
                logging.error(f"Failed to convert {input_path} - Error: {e}")

if __name__ == "__main__":
    input_directory = "/path/to/your/video_files"
    output_directory = "/path/for/your/gifs"

    logging.info("Starting MP4 to GIF conversion...")
    convert_mp4_to_gif(input_directory, output_directory)
    logging.info("Conversion process completed.")
