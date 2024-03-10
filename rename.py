import os

# Specify the directory containing the files
directory = r'CollectedImages\Thanks'

# List all files in the directory
files = os.listdir(directory)

# Loop through each file and rename it
i=1
for filename in files:
    # Define the new name for the file (you can manipulate the filename as you wish here)
    new_string = f"thanks_{i}.jpg"
    new_name = filename.replace(filename, new_string)  # Example: replace 'old_string' with 'new_string'
    
    # Construct the full paths of the old and new names
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    i=i+1
