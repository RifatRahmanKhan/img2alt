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
    parts = line.strip().split(",")

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
print(captions_array)
