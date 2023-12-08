import cv2
import os

# Set the input video file path and output directory
input_video_path = 'video1.webm'
output_directory = 'output_images/'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Set the desired frame rate for the output images (24 fps in this case)
desired_fps = 24

# Calculate the frame interval to capture frames at the desired rate
frame_interval = int(fps / desired_fps)

# Initialize a counter for the output image filenames
frame_count = 0

# Loop through the video frames and save images at the desired frame rate
while True:
    ret, frame = cap.read()
    
    # Break the loop if we have reached the end of the video
    if not ret:
        break
    
    # Save the frame as an image
    if frame_count % frame_interval == 0:
        output_image_path = os.path.join(output_directory, f'frame_{frame_count:04d}.png')
        cv2.imwrite(output_image_path, frame)
        print(frame_count)
    
    frame_count += 1

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()

print(f"Images saved at {desired_fps} fps in '{output_directory}'")
