# MP4-To-GIF Converter

Convert MP4 files into GIFs.

## Set Up

### Programs Needed

1. [Git](https://git-scm.com/downloads)
2. [Python](https://www.python.org/downloads/) (When installing on Windows, make sure you check the "[Add python 3.xx to PATH](https://hosting.photobucket.com/images/i/bernhoftbret/python.png)" box.)

### Steps

1. Install the above programs.
2. Open a shell window (for Windows open PowerShell, for MacOS open Terminal and for Linux open your distro's terminal emulator).
3. Clone this repository using git by running the following command: `git clone https://github.com/devbret/mp4-to-gif`.
4. Navigate to the repo's directory by running: `cd mp4-to-gif`.
5. Install the needed dependencies for running the script by running: `pip install -r requirements.txt`.
6. Add paths for your input/MP4 files (on line 40 of the app.py script) and output/GIF files (on line 41 on the app.py script). Also make sure to save the script file after changing the paths.
7. Run the script with the command `python3 app.py`.
8. After the script has completed, visit the output directory where your new GIFs are located.

## Please Note

The file size of the GIFs generated using this program are dependent on the size of the original MP4 files. And therefore may be extraordinarily large after processing. Please consider this.
