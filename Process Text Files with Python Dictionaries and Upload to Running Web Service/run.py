#! /usr/bin/env python3

import os
import requests


feedback_directory = "/data/feedback"

files = os.listdir(feedback_directory)

def readlines(files):
    file_path = os.path.join(feedback_directory, files)
    try:
        with open(file_path) as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        lines = []
    except PermissionError:
        print(f"Permission denied for {file_path}")
        lines = []
    return lines

feedback = []
keys = ['title', 'name', 'date', 'feedback']
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

url = "http://localhost/feedback/"

for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")
