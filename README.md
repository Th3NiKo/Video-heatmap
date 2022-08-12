# Video-heatmap

## Table of contents

* [Description](#description)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Example output](#output)

## Description

Script for heatmap generation (for movement) from single video with static camera.

**Program pipeline:**

1. Load frame
2. Substract background
3. Accumulate movement
4. Normalize accumulated frame (for view only)
5. Apply heatmap colormap
6. Optional: Supervise with original frame (check --alpha parameter)
7. Save new frame

**Program structure:**

* video_heatmap.py - main program with whole pipeline implemented
* vision.py - image operations module
* arguments_parser.py - manage script arguments

## Getting Started

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J10ZQep7UX2BU3MnaWLJbwfe9nBuq9lP?usp=sharing)

### Quick start

Tested with python 3.8.3.

Libraries used: [opencv-python](https://github.com/opencv/opencv-python). (Tested on ver. 4.4.0)\
You can install it using pip.

```bash
pip install -r requirements.txt
```

Check if script works and show help

```bash
python video_heatmap.py -h
```

## Usage

```bash
video_heatmap.py [-h] -f VIDEO_FILE [-a VIDEO_ALPHA] [-d] [-o VIDEO_OUTPUT] [-s VIDEO_SKIP] [-t TAKE_EVERY]

optional arguments:
  -h, --help            show this help message and exit
  -f VIDEO_FILE, --file VIDEO_FILE
                        Video file path for which heatman will be created. Example: input.mp4
  -a VIDEO_ALPHA, --alpha VIDEO_ALPHA
                        Optional parameter to adjust alpha between heatmap and original video frames.
                        Value between 0.0-1.0 represent what part of original video heatmap gonna take. 
                        Default: 0.9
  -d, --disable         Disable live view of heatmap generation.
  -o VIDEO_OUTPUT, --output VIDEO_OUTPUT
                        Adjust name of output files. Script creates two files one video .mp4 and one image .png.
                        Default: output
  -s VIDEO_SKIP, --skip VIDEO_SKIP
                        Skip first number of frames in order to warm up background substraction alghoritm.
                        Default: 200 frames
  -t TAKE_EVERY, --take-every TAKE_EVERY
                        In order to speed up process it is possible to skip frames and take every x frame.
                        Default: 1 (take all frames).
```

Example usage:

```bash
python video_heatmap.py -f input.mp4 -o output_name
```

If u want to **DISABLE LIVE VIEW** of process use -d flag

```bash
python video_heatmap.py -f input.mp4 -o output_name -d
```

If u want to check **SPEED UP PROCESS** you can adjust -t flag to take every x frame. \
Example: Take every third frame

```bash
python video_heatmap.py -f input.mp4 -o output_name -t 3
```

It is good idea to warm up background substraction alghoritm and skip first x frames. \
If u want to do it **ADJUST NUMBER OF WARMUP FRAMES** use -s flag

```bash
python video_heatmap.py -f input.mp4 -o output_name -s 100
```

If u want to **CHANGE ALPHA BETWEEN ORIGINAL AND HEATMAP** use -a flag

```bash
python video_heatmap.py -f input.mp4 -o output_name -a 0.5
```

## Example output

Original video:

[![Original video](https://img.youtube.com/vi/MNn9qKG2UFI/hqdefault.jpg)](https://youtu.be/MNn9qKG2UFI)

Output of script:

[![Output video](https://img.youtube.com/vi/UhYFcNcXlvs/hqdefault.jpg)](https://youtu.be/UhYFcNcXlvs)
