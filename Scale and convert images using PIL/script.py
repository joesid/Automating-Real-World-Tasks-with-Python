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

file_list = os.listdir(dir)

for old_filename in file_list:
   if os.path.isfile(os.path.join(dir, old_filename)):
      new_filename = old_filename + ".tiff"
      os.rename(os.path.join(dir, old_filename),os.path.join(dir, new_filename))

      file_list2 = os.listdir(dir)



      sav_path = script_dir + "/opt/icons/"

      for filename in os.listdir(sav_path):

           file_path = os.path.join(sav_path, filename)

           image = Image.open(file_path)

      for file_name in file_list2:
         source_file = os.path.join(dir, file_name)
         destination_file = os.path.join(sav_path, file_name)
         shutil.copy(source_file, destination_file)