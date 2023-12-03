import numpy as np

# Set the path to the captions.txt file
captions_file_path = "../archive/captions.txt"

# Read captions from the file
with open(captions_file_path, "r") as file:
    captions_data = file.readlines()

# Create a dictionary to store the first caption for each image
first_captions_dict = {}

# Extract the first caption for each image
for line in captions_data:
    parts = line.strip().split(",", 1)

    # Check if the line has the expected format
    if len(parts) == 2:
        image_id = parts[0]
        caption = parts[1]

        # Add the first caption for each image to the dictionary
        if image_id not in first_captions_dict:
            first_captions_dict[image_id] = caption
    else:
        print(f"Skipping line: {line}")

# Convert the dictionary values (captions) to a numpy array
captions_array = np.array(list(first_captions_dict.values()))

# Print the captions array
print(len(captions_array))



import os
import shutil
import random

# Set the path to the images folder
images_folder_path = "../archive/images"

# Set the ratio for training and testing data
train_ratio = 0.8

# Get the list of image files
image_files = [f for f in os.listdir(images_folder_path) if f.endswith('.jpg')]

# Shuffle the list of image files
random.shuffle(image_files)

# Calculate the number of images for training and testing
num_train = int(len(image_files) * train_ratio)
num_test = len(image_files) - num_train

# Create directories for training and testing images
train_folder = "path/to/your/train/folder"
test_folder = "path/to/your/test/folder"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Copy images to the training folder
for i in range(num_train):
    image_file = image_files[i]
    src_path = os.path.join(images_folder_path, image_file)
    dst_path = os.path.join(train_folder, image_file)
    shutil.copy(src_path, dst_path)

# Copy images to the testing folder
for i in range(num_train, num_train + num_test):
    image_file = image_files[i]
    src_path = os.path.join(images_folder_path, image_file)
    dst_path = os.path.join(test_folder, image_file)
    shutil.copy(src_path, dst_path)

print(f"Number of training images: {num_train}")
print(f"Number of testing images: {num_test}")



