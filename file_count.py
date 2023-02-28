import os

# set the path to the folder
folder_path = "C:\Users\jmica\OneDrive\Desktop\webscraper\pdfthumbs"

# get the list of files in the folder
files = os.listdir(folder_path)

# count the number of files
num_files = len(files)

# print the number of files
print(f"There are {num_files} files in the folder.")
