"""
Module for preparing arguments parser.
"""

import argparse

def prepare_parser():
    """Prepare parser with arguments and return it."""

    parser = argparse.ArgumentParser()

    # File path
    parser.add_argument("-f", "--file", action="store", dest="video_file",
                        help="Video file path for which heatman will \
                              be created. Example: input.mp4",
                        required=True)

    # Alpha between original frame and heatmap
    parser.add_argument("-a", "--alpha", action="store", dest="video_alpha",
                        help="Optional parameter to adjust alpha between \
                              heatmap and original video frames. Value between \
                              0.0-1.0 represent what part of original video heatmap \
                              gonna take. Default: 0.9",
                        required=False, default=0.9, type=float)

    # Disable live view
    parser.add_argument("-d", "--disable", action="store_true", dest="video_disable",
                        help="Disable live view of heatmap generation.",
                        required=False, default=False)

    # Output name
    parser.add_argument("-o", "--output", action="store", dest="video_output",
                        help="Adjust name of output files. Script creates two files \
                              one video .mp4 and one image .png. Default: output",
                        required=False, default="output")

    # Skip first frames
    parser.add_argument("-s", "--skip", action="store", dest="video_skip",
                        help="Skip first number of frames in order to warm up background \
                              substraction alghoritm. Default: 200 frames",
                        required=False, default=200, type=int)

    # Take every x frame
    parser.add_argument("-t", "--take-every", action="store", dest="take_every",
                        help="In order to speed up process it is possible to skip frames and \
                            take every x frame. Default: 1 (take all frames).",
                        required=False, default=1, type=int)
    return parser
