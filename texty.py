import glob
import subprocess

poppler_path = r'C:\Program Files\poppler-0.68.0\bin'

def extract_text_from_pdf(pdf_path):
    result = subprocess.run([poppler_path + '\\pdftotext', pdf_path, '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

pdf_files = glob.glob('C:\\Users\\jmica\\OneDrive\\Desktop\\webscraper\\pdfs\\*.pdf')
for pdf_file in pdf_files:
    pdf_text = extract_text_from_pdf(pdf_file)
    with open(pdf_file[:-4] + '.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(pdf_text)
