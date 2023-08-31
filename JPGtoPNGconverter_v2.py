# Converts .jpg images to .png
# Asks user for source and ouput folders

# Import libraries
import os
from PIL import Image


def check_slash(string):
    '''
    Checks if a string contains '/' as the last character
    '''
    if string[-1] != '/':
        string = string + '/'
    return string


# Get source location from user
location = check_slash(input("Enter source folder: "))

# Check if source location exists, otherwise ask for input again
while not os.path.exists(location):
    location = check_slash(input("Folder does not exist. Please try again: "))

# Get output location from user
new_folder = check_slash(input("Enter output folder: "))

#Create output folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Convert .jpg files in source folder to .png in output folder
for file in os.listdir(location):
    if '.jpg' in file:
        img = Image.open(location + file)
        name = os.path.splitext(file)[0]
        img.save(new_folder + name + '.png', 'png')
print("All done!")
