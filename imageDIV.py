import os

# set the folder where the images are located
folder_path = "C:/Users/jmica/OneDrive/Desktop/webscraper/pdfthumbs"

# get the list of image file names in the folder
image_files = os.listdir(folder_path)

# create a list of image src tags to be inserted into the divs
image_src_tags = [f'<img src="{os.path.join(folder_path, img)}" style="max-width: 100%; max-height: 100%; display: block; margin: auto;" />' for img in image_files]

# calculate the number of rows and columns needed for the grid
num_images = len(image_files)
num_rows = (num_images + 2) // 3  # add 2 and integer divide by 3 to round up
num_cols = min(num_images, 3)

# create a list of div tags that follow the grid-column style
divs = []
for row in range(num_rows):
    for col in range(num_cols):
        index = row * 3 + col
        if index >= num_images:
            break
        divs.append(f'<div style="grid-column: {col + 1} / {col + 2}; grid-row: {row + 1} / {row + 2}; border: 1px solid black;">{image_src_tags[index]}</div>')

# create the final HTML code
html_code = f'<div style="display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat({num_rows}, 300px); grid-gap: 5px; border: 1px solid black;">\n  {"".join(divs)}\n</div>'

# print the HTML code
print(html_code)

# # get the list of image file names in the folder
# image_files = os.listdir(folder_path)

# # create a list of image src tags to be inserted into the divs
# image_src_tags = [f'<img src="{os.path.join(folder_path, img)}" />' for img in image_files]

# # get the number of images in the folder
# num_images = len(image_files)

# # calculate the number of rows needed to display all the images
# num_rows = (num_images + 2) // 3

# # create additional div tags to match the grid-column style
# for row in range(1, num_rows + 1):
#     for col in range(1, 4):
#         if (row - 1) * 3 + col <= num_images:
#             image_index = (row - 1) * 3 + col - 1
#             image_div = f'<div style="grid-column: {col} / {col + 1}; grid-row: {row} / {row + 1};border: 1px solid black;">{image_src_tags[image_index]}</div>'
#             print(image_div)
#         else:
#             empty_div = f'<div style="grid-column: {col} / {col + 1}; grid-row: {row} / {row + 1};border: 1px solid black;"></div>'
#             print(empty_div)
