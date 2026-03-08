# MP4-To-GIF Converter

Automates the conversion of multiple MP4 video files into high-quality GIFs using the moviepy library.

## Overview

The MP4-To-GIF Converter takes all `.mp4` files from a specified input directory, processes each one and saves the converted GIFs into an output directory. The script ensures both input and output directories are properly handled. The conversion itself uses `ffmpeg` for efficiency, matching the GIF frame rate to the source video to preserve visual smoothness while minimizing quality loss.

The program also features a structured logging system to track progress and handle errors. It records every major event, such as when a file starts processing, completes successfully, or fails due to an exception. These logs are written both to the console and a file named `conversion.log`.

Overall, the program provides a reliable, automated and transparent way to batch-convert MP4 videos into GIF animations, making it useful for content creators, developers and digital artists who need to generate GIFs from video clips efficiently.

## Set Up Instructions

Below are the required software and initial steps for running this application.

### Programs Needed

1. [Git](https://git-scm.com/downloads)

2. [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository using git by running the following command: `git clone git@github.com:devbret/mp4-to-gif.git`

4. Navigate to the repo's directory by running: `cd mp4-to-gif`

5. Install the needed dependencies for running the script: `pip install -r requirements.txt`

6. Add and save paths for your input/MP4 files (on line 40 of the `app.py` script) and output/GIF files (on line 41 on the `app.py` script)

7. Run the script with the command: `python3 app.py`

8. After the script has completed, open the output directory where your new GIFs are located

## Please Note

The file sizes of the GIFs generated using this program are dependent on the file sizes of the original MP4 files. Those GIF files may therefore be extraordinarily large after processing. Please consider this before running the software.
