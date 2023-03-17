import rembg
import os
from PIL import Image

# Set the path to the input and output folders
input_folder = "Frames"
output_folder = "Frames/Removed_BG"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image file
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Load the image and remove the background
        image_path = os.path.join(input_folder, filename)
        with open(image_path, "rb") as f:
            image = f.read()
        output = rembg.remove(image)

        # Save the resulting image in the output folder
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "wb") as f:
            f.write(output)

# Release any resources used by the rembg module
rembg.shutdown()
