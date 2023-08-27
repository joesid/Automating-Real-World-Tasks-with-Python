#!/usr/bin/env python3

import os
from PIL import Image
import shutil

# Find Script Directory
directory = "images/"

# Identify Output directory
output_dir = "/opt/icons/"

# Loop through images directory
for filename in os.listdir(directory):
    if filename != ".DS_Store":
        image = Image.open(os.path.join(directory, filename))
        image = image.rotate(-90)
        image = image.resize((128, 128))
        image = image.convert("RGB")
        image.save(os.path.join(output_dir, filename + ".jpeg"))
