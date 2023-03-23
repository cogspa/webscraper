# Define the dictionary of keywords and their corresponding letters
my_dict = {'A': ['ALT', 'ALT', 'Alt', 'Alt', 'Alt', 'ALT', 'ALT', 'Alt', 'Alt', 'Alt', 'Alt'], 
           'S': ['Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Start', 'Sustainability'], 
           'B': ['Boosters', 'Boosters', 'Battery', 'Battery', 'Brakes', 'Battery'], 
           'C': ['Clutch', 'Clutch', 'Calipers'], 
           'W': ['Winter', 'Winter', 'Winter', 'Winter', 'Winter', 'Winter'], 
           'M': ['MasterCylinder', 'MasterCylinder', 'MC', 'MC', 'MC', 'MC', 'MC'], 
           'F': ['Faulty_Sensor', 'Faulty_Sensor'], 
           'H': ['Hub', 'Hub', 'Hub', 'Hub', 'Hub', 'Hub', 'Hub', 'Hub', 'Hydro-Booster', 'Hydro-Booster', 'Hub'], 
           'N': ['No-Charge-Issue', 'No-Charge-Issue', 'Neg-Side-Circuit-Signs', 'Neg-Side-Circuit-Signs'], 
           'T': ['Turbo', 'Turbo', 'Turbo', 'Turbo', 'Turbo'], 
           'P': ['Piston', 'Piston'], 
           'R': ['RE'], 
           'V': ['Vacuum-Booster', 'Vacuum-Boster']}

# Open the input file
with open('output.rtf', 'r', encoding='unicode_escape') as f:

    # Read the file contents
    file_contents = f.read()

    # Create a new file
    with open('NewList7.rtf', 'w', encoding='unicode_escape') as new_file:
        
        # Loop through the dictionary keys
        for key in my_dict.keys():
            
            # Write the key to the new file with the appropriate RTF syntax for bolding
            new_file.write('{\\b ' + key + '}\\line\n')
            
            # Loop through the filenames
            for filename in file_contents.split('\n'):
                
                # Check if the filename contains any words in the current dictionary key
                if any(word.lower() in filename.lower() for word in my_dict[key]):
                    
                    # Write the filename to the new file with the appropriate RTF syntax for a new line
                    new_file.write(filename + '\\line\n')
            
            # Add a blank line between sections
            new_file.write('\\line\n')
