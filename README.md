# MP4-To-GIF Converter

Automate batch conversion of `.mp4` video files into `.gif` animations with directory handling and structured logging for progress and errors.

## Overview

The MP4-To-GIF Converter takes all `.mp4` files from a specified input directory, processes each one and saves the converted GIFs into an output directory. The script ensures both input and output directories are properly handled. The conversion itself uses `ffmpeg` for efficiency, matching the GIF frame rate to the source video to preserve visual smoothness while minimizing quality loss.

The program also features a structured logging system to track progress and handle errors. It records every major event, such as when a file starts processing, completes successfully, or fails due to an exception. These logs are written both to the console and a file named `conversion.log`.

Overall, the program provides a reliable, automated and transparent way to batch-convert MP4 videos into GIF animations, making it useful for content creators, developers and digital artists who need to generate GIFs from video clips efficiently.

## Set Up Instructions

Below are the required software programs and initial steps for running this application on a Linux machine.

### Programs Needed

1. [Git](https://git-scm.com/downloads)

2. [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/mp4-to-gif.git`

4. Navigate to the repo's directory: `cd mp4-to-gif`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate the virtual environment: `source venv/bin/activate`

7. Install the needed dependencies for running the script: `pip install -r requirements.txt`

8. Add paths for your `.mp4` files (on line 40 of the `app.py` script) and `.gif` files (on line 41 on the `app.py` script)

9. Add your `.mp4` files to the designated input directory

10. Run the Python script: `python3 app.py`

11. Open the output directory where your new `.gif` files are located after the script has completed

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Configure logging record conversion progress and errors to both the console and a `conversion.log` file

- Check whether the input directory exists before attempting to process any video files

- Create the output directory automatically if it does not already exist

- Find each `.mp4` file in the input directory and convert it into a `.gif` file using `MoviePy` and `FFmpeg`

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).

### Please Note

The sizes of the `.gif` files generated using this program are dependent on the sizes of the original `.mp4` files. Those `.gif` files may be extraordinarily large after processing. Please consider this before running the software.
