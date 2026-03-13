import os
import shutil

path = "files"   # folder to organize

files = os.listdir(path)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        folder = "images"
    elif file.endswith(".pdf"):
        folder = "pdf"
    elif file.endswith(".txt"):
        folder = "text"
    else:
        folder = "others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully")
