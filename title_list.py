import os

# Get the path of the folder containing the text documents
folder_path = "/path/to/folder"

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Create a new file to store the titles
new_file = open("titles.txt", "w")

# Loop through each file in the folder
for file in files:
    # Check if the file is a text document
    if file.endswith(".txt"):
        # Open the file
        with open(os.path.join(folder_path, file), "r") as f:
            # Read the first line of the file (assuming the title is in the first line)
            title = f.readline().strip()
            # Write the title to the new file
            new_file.write(title + "\n")

# Close the new file
new_file.close()
