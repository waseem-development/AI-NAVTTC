# ============================================================
# VIDEO PROCESSING WORKFLOW
# ============================================================

# Capture Video
# ------------------------------------------------------------
# Capturing video means reading frames either from:
#   - a webcam (live stream)
#   - a video file (stored on disk)
# In OpenCV, this is done using:
#   cap = cv2.VideoCapture(source)
# where source can be:
#   0 → default webcam
#   "video.mp4" → video file


# Save Video
# ------------------------------------------------------------
# Saving video means writing processed frames into a new video file.
# OpenCV uses VideoWriter for this:
#   out = cv2.VideoWriter(...)
# You take each processed frame and write it:
#   out.write(frame)
# This creates a new video with your modifications applied.


# Web Cam Stream
# ------------------------------------------------------------
# A webcam stream is a continuous flow of frames coming from your camera.
# Instead of loading once, frames are captured in a loop:
#   while True:
#       ret, frame = cap.read()
# This allows real-time processing (like filters, detection, etc.)


# Processed Video File
# ------------------------------------------------------------
# A processed video file is a new video created after applying operations
# (like grayscale, blur, edge detection) to each frame of the original video.
# Example:
#   Original video → apply filter → save as new video file


# Process Frames
# ------------------------------------------------------------
# Processing frames means applying image operations to each frame.
# Since a frame is just an image, all image techniques apply:
#   - grayscale conversion
#   - filtering (blur)
#   - edge detection
#   - drawing shapes/text
# Each frame is processed individually inside a loop.


# ============================================================
# VIDEO COMPONENTS
# ============================================================

# What is a Video?
# ------------------------------------------------------------
# A video is a sequence of images (frames) displayed rapidly.
# When these images are shown one after another at high speed,
# our brain perceives continuous motion.
# This is known as persistence of vision.


# What is a Frame?
# ------------------------------------------------------------
# A frame is a single image in a video.
# A video is made up of many frames.
# Each frame can be processed just like a normal image.


# FPS (Frames Per Second)
# ------------------------------------------------------------
# FPS tells how many frames are shown in one second.
# Common values:
#   30 FPS → standard video
#   60 FPS → smoother motion
# Higher FPS = smoother video but more data to process.


# Fundamental Concept of Video
# ------------------------------------------------------------
# Video processing = processing many images (frames) in sequence.
# If you understand image processing, you already understand
# the core idea behind video processing.


# ============================================================
# WEBCAM
# ============================================================

# What is a Webcam?
# ------------------------------------------------------------
# A webcam is a camera connected to a computer (built-in or external).
# It captures live video and sends frames to the system in real time.


# Purpose of a Webcam
# ------------------------------------------------------------
# - Video calls (Zoom, Meet, etc.)
# - Real-time computer vision applications
# - Face detection, gesture recognition
# - Surveillance and monitoring systems


# ============================================================
# FRAME-BY-FRAME PROCESSING
# ============================================================

# What is Frame-by-Frame Processing?
# ------------------------------------------------------------
# Instead of processing a full video at once,
# we process one frame at a time in a loop.


# How Video is Processed Frame-by-Frame
# ------------------------------------------------------------
# Step-by-step:
# 1. Capture frame from video/webcam
#       ret, frame = cap.read()
#
# 2. Apply processing (like grayscale, blur, etc.)
#       processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# 3. Display or save the processed frame
#       cv2.imshow("Output", processed)
#
# 4. Repeat this for every frame in a loop
#
# This creates real-time video processing.


# Key Idea
# ------------------------------------------------------------
# Frame-by-frame processing = applying image operations repeatedly
# on a continuous stream of frames.

# So:
#   Image Processing → One Image
#   Video Processing → Many Images (Frames in a loop)

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret means return: ret=True/False, frame=image

    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam Freed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()