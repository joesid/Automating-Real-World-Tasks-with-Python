#!/usr/bin/env python3

import os
from PIL import Image
import shutil

# Find Script Directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Identify Image directory
dir = script_dir + "/images"

# Check if /opt/icons  directory exist
icons_dir = os.path.join(dir, "opt/icons")
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)


# Assign save directory
sav_path = dir + "/opt/icons/"
# sav_path = script_dir + "/opt/icons/"

# Change directory permission
os.chmod(sav_path, 0o777)

# Directory containing list of image files
file_list = os.listdir(dir)

# Move Images contents to Icon Folder
for file_name in file_list:
    source_file = os.path.join(dir, file_name)
    destination_file = os.path.join(sav_path, file_name)
    shutil.move(source_file, destination_file)

for filename in os.listdir(sav_path):
    file_path = os.path.join(sav_path, filename)

    image = Image.open(file_path)

    rotated_image = image.rotate(90)

    resized_image = rotated_image.resize((128, 128))
    rgb_image = resized_image.convert("RGB")
    rgb_image.save(file_path, "JPEG")

