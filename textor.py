import os

# Get the path of the folder containing the files
folder_path = "C:/Users/jmica/OneDrive/Desktop/webscraper/pdfthumbs2"

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Create an empty list to store the file names
file_list = []

# Loop through each file in the folder
for file in files:
    # Replace the forward slash with a carriage return
    file_name = file.replace("/", "\n")
    # Append the modified file name to the list
    file_list.append(file_name)

# Write the list to a file
with open("file_list3.txt", "w") as f:
    f.writelines(file_list)