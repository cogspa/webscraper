import os
from pdf2image import convert_from_path

# The path to the PDF files
pdf_dir = "C:\\Users\\jmica\\OneDrive\\Desktop\\webscraper\\QBBS_SS"


# The path to save the PNG files
png_dir = "C:\\Users\\jmica\\OneDrive\\Desktop\\webscraper\\SS"


# Loop through all PDF files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        images = convert_from_path(pdf_path, 500, poppler_path = r'C:\Program Files\poppler-0.68.0\bin')
        png_path = os.path.join(png_dir, f"{os.path.splitext(filename)[0]}.png")
        images[0].save(png_path, "PNG")