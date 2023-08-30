# Converts .jpg images to .png
# Takes input and output folders as arguments

# Import libraries
import sys
import os
from PIL import Image

# Get source folder and output folder
location = str(sys.argv[1])
new_folder = str(sys.argv[2])

# Create output folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Convert .jpg files in source folder to .png in output folder
for file in os.listdir(location):
    if '.jpg' in file:
        img = Image.open(location + file)
        name = os.path.splitext(file)[0]
        img.save(new_folder + name + '.png', 'png')
        print("All done!")
