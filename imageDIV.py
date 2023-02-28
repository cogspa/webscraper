import os

# set the folder where the images are located
folder_path = "C:/Users/jmica/OneDrive/Desktop/webscraper/pdfthumbs"

# get the list of image file names in the folder
image_files = os.listdir(folder_path)

# create a list of image src tags to be inserted into the divs
image_src_tags = [f'<img src="{os.path.join(folder_path, img)}" />' for img in image_files]

# get the number of images in the folder
num_images = len(image_files)

# calculate the number of rows needed to display all the images
num_rows = (num_images + 2) // 3

# create additional div tags to match the grid-column style
for row in range(1, num_rows + 1):
    for col in range(1, 4):
        if (row - 1) * 3 + col <= num_images:
            image_index = (row - 1) * 3 + col - 1
            image_div = f'<div style="grid-column: {col} / {col + 1}; grid-row: {row} / {row + 1};border: 1px solid black;">{image_src_tags[image_index]}</div>'
            print(image_div)
        else:
            empty_div = f'<div style="grid-column: {col} / {col + 1}; grid-row: {row} / {row + 1};border: 1px solid black;"></div>'
            print(empty_div)
