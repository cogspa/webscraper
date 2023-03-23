import re

# Create an empty dictionary
parts_dict = {}

# Open the rtf file
with open('output5.rtf', 'r') as f:
    # Read the file
    file_text = f.read()

    # Find all the bold text using regex
    bold_text = re.findall(r'\\b (.+?)\\b0', file_text)

    # Loop through each bold text and create a dictionary entry
    for text in bold_text:
        # Split the text into words
        words = text.split()

        # Get the first initial of each word and create a key
        key = ''.join([word[0].upper() for word in words])

        # Check if the key already exists in the dictionary, if not add it with an empty list as the value
        if key not in parts_dict:
            parts_dict[key] = []

        # Add the text as a value to the key
        parts_dict[key].append(text)

# Print the dictionary
print(parts_dict)
