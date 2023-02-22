import os
import chardet
from gensim.summarization import summarize

def summarize_text_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    encoding = chardet.detect(data)['encoding']
    try:
        with open(file_path, encoding=encoding) as file:
            text = file.read()
    except (UnicodeDecodeError, LookupError):
        try:
            with open(file_path, encoding='cp1252') as file:
                text = file.read()
        except UnicodeDecodeError:
            with open(file_path, encoding='ISO-8859-1') as file:
                text = file.read()
    return summarize(text)

def summarize_folder(folder_path):
    summaries = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            summary = summarize_text_file(file_path)
            summaries.append(summary)
    return summaries

folder_path = r"C:\Users\jmica\OneDrive\Desktop\webscraper\pdfs"
summaries = summarize_folder(folder_path)
for summary in summaries:
    print(summary)
