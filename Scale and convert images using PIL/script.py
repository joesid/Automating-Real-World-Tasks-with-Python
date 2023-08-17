#!/usr/bin/env python3

import os
from PIL import Image
import shutil



script_dir = os.path.dirname(os.path.abspath(__file__))
#print("script directory: ", script_dir)


dir = script_dir + "/images"

if os.path.exists(script_dir + "/opt/icons/"):
   print("folder already created")
else:
   os.makedirs(script_dir + "/opt/icons/")

sav_path = script_dir + "/opt/icons/"

#Change directory permission
os.chmod(sav_path, 0o777)

for filename in os.listdir(dir):
   file_path = os.path.join(dir, filename)

   image = Image.open(file_path)

   rotated_image = image.rotate(90)

   resized_image = rotated_image.resize((128, 128))

   rgb_image = resized_image.convert("RGB")

   rgb_image.save(sav_path, "JPEG")

# for filename in os.listdir(dir):
#    shutil.copy2(dir, sav_path)