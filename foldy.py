import os
import shutil

# Get the path of the folder containing the files
folder_path = "/path/to/folder"

# Define the criteria for creating subfolders
subfolders = {"alternators": ["alt", "alternator"], "boosters": ["booster"]}

# Loop through each file in the folder
for file in os.listdir(folder_path):
    # Get the full path of the file
    file_path = os.path.join(folder_path, file)
    # Check if the file is a file (not a folder) and not hidden
    if os.path.isfile(file_path) and not file.startswith("."):
        # Loop through the subfolders and check if the file name matches any criteria
        for subfolder_name, criteria in subfolders.items():
            for criterion in criteria:
                if criterion in file.lower():
                    # Create the subfolder if it does not exist
                    subfolder_path = os.path.join(folder_path, subfolder_name)
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                    # Copy the file to the subfolder
                    shutil.copy(file_path, subfolder_path)
                    break # Stop checking criteria once a match is found

