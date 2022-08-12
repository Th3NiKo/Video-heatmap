# -*- coding: utf-8 -*-
"""Script for heatmap generation from single video with static camera.

Program pipeline:
    1. Load frame
    2. Substract background
    3. Accumulate movement
    4. Normalize accumulated frame (for view only)
    5. Apply heatmap colormap
    6. Optional: Supervise with original frame (check --alpha parameter)
    7. Save new frame
"""

# pylint: disable=no-member

import cv2
import numpy as np

import vision
import arguments_parser

def main():
    """
    Whole heatmap pipeline creation.
    """
    parser = arguments_parser.prepare_parser()
    args = parser.parse_args()

    capture = cv2.VideoCapture(args.video_file)
    background_subtractor = cv2.createBackgroundSubtractorKNN()

    read_succes, video_frame = capture.read()

    height, width, _ = video_frame.shape
    frames_number = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    video = cv2.VideoWriter(args.video_output + ".mp4", fourcc, 30.0, (width, height))
    accumulated_image = np.zeros((height, width), np.uint8)

    count = 0

    while read_succes:
        read_succes, video_frame = capture.read()
        if read_succes:
            background_filter = background_subtractor.apply(video_frame)
            if count > args.video_skip and count % args.take_every == 0:

                erodated_image = vision.apply_morph(background_filter,
                                                    morph_type=cv2.MORPH_ERODE,
                                                    kernel_size=(5,5))
                accumulated_image = vision.add_images(accumulated_image, erodated_image)
                normalized_image = vision.normalize_image(accumulated_image)
                heatmap_image = vision.apply_heatmap_colors(normalized_image)
                frames_merged = vision.superimpose(heatmap_image, video_frame, args.video_alpha)

                if not args.video_disable:
                    cv2.imshow("Main", frames_merged)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                video.write(frames_merged)
                if count % 100 == 0:
                    print(f"Progress: {count}/{frames_number}")
            count += 1

    cv2.imwrite(args.video_output + ".png", heatmap_image)
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
