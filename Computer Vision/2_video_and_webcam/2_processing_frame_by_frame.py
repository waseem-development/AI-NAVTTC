# Frame by Frame Processing
# Why?
#  - Draw
#  - Detect (faces, eyecolor)
#  - Analyze
#  - Specific Time

# How to save a video as a file?
# cv2.VideoWriter(filename, codec, fps, frame_size)
# codec is a compression format


import cv2

# Open the default webcam (0 = built-in camera)
camera = cv2.VideoCapture(0)

# ------------------------------------------------------------
# .get() method → used to READ properties from the camera/video
# ------------------------------------------------------------
# It asks OpenCV:
# "What is the current value of this property?"
#
# Think of it like:
#   camera.get(property_id) → returns value

# ------------------------------------------------------------
# CAP_PROP_FRAME_WIDTH
# ------------------------------------------------------------
# Constant that represents:
#   → width of each frame (in pixels)
# Example: 640, 1280, etc.
#
# So this line means:
#   "Get the width of frames coming from the camera"
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))

# ------------------------------------------------------------
# CAP_PROP_FRAME_HEIGHT
# ------------------------------------------------------------
# Constant that represents:
#   → height of each frame (in pixels)
# Example: 480, 720, 1080, etc.
#
# So this means:
#   "Get the height of frames from the camera"
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


# ------------------------------------------------------------
# cv2.VideoWriter_fourcc(*"XVID")
# ------------------------------------------------------------
# FOURCC = "Four Character Code"
# It defines the VIDEO COMPRESSION FORMAT (codec)
#
# "XVID" means:
#   → Xvid MPEG-4 compression
#   → reduces file size while keeping quality
#
# Why *"XVID"?
# Because Python passes it as characters:
#   'X', 'V', 'I', 'D'
#
# Internally OpenCV converts it into a numeric codec ID
codec = cv2.VideoWriter_fourcc(*"XVID")


# ------------------------------------------------------------
# cv2.VideoWriter(...)
# ------------------------------------------------------------
# This is used to SAVE video frames into a file.

recorder = cv2.VideoWriter(
    "./outputs/my_video.avi",  # output file path
    codec,                      # compression format (XVID here)
    20,                         # FPS (frames per second)
    (frame_width, frame_height) # size of each frame (width, height)
)

# ------------------------------------------------------------
# Parameters explained:
# ------------------------------------------------------------

# 1. "./outputs/my_video.avi"
#    → file name + format
#    → AVI container (works well with XVID)

# 2. codec
#    → tells HOW to compress video
#    → without codec, file would be huge/raw

# 3. 20 (FPS)
#    → frames per second
#    → higher = smoother video but larger file
#    → lower = choppy but smaller file

# 4. (frame_width, frame_height)
#    → size of video frames
#    → MUST match camera frames exactly
#    → otherwise video will be corrupted or not saved


# ------------------------------------------------------------
# Frame-by-frame processing loop
# ------------------------------------------------------------
while True:

    # read() returns:
    # success → True/False if frame was read
    # image → actual frame (numpy array)
    success, image = camera.read()

    if not success:
        break

    # Write frame into video file
    # → this is where recording actually happens
    recorder.write(image)

    # Show live camera feed
    cv2.imshow("Recording Live", image)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ------------------------------------------------------------
# Release resources
# ------------------------------------------------------------
# camera.release() → frees webcam hardware
# recorder.release() → finalizes & saves video file
# cv2.destroyAllWindows() → closes GUI windows
camera.release()
recorder.release()
cv2.destroyAllWindows()