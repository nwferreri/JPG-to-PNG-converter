# give folder name Pokedex/ new/  new doesn't exist yet
# program looks in pokedex folder
# grab first and second arguments using sys module
# check if new/ exists, if not create it
# loop through Pokedex, convert images to png
# save images to new folder

import sys
import os  # grab path
from PIL import Image

location = str(sys.argv[1])
new_folder = str(sys.argv[2])

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(location):
    if '.jpg' in file:
        img = Image.open(location + file)
        name = os.path.splitext(file)[0]
        img.save(new_folder + name + '.png', 'png')
        print("All done!")
