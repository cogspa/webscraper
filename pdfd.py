import requests
import zipfile
import io

url = "https://motorcarparts.com/brand/quality-built-black/" # replace with the actual URL
response = requests.get(url)
pdf_links = []

# extract all PDF links from the page
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all("a"):
    if link.get("href").endswith(".pdf"):
        pdf_links.append(link.get("href"))

# create a BytesIO object to store the ZIP file
zip_file = io.BytesIO()

# create the ZIP file and add the PDFs to it
with zipfile.ZipFile(zip_file, "w") as my_zip:
    for pdf_link in pdf_links:
        pdf_response = requests.get(pdf_link)
        my_zip.writestr(pdf_link.split("/")[-1], pdf_response.content)

# write the ZIP file contents to disk
with open("pdfs4.zip", "wb") as f:
    f.write(zip_file.getvalue())