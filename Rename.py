import os
from os.path import join, getmtime

# Specify the directory path you want to sort and rename files in
directory_path = '/home/unknown/Downloads/Javascript'

# List the files in the directory and their modification times
files = [(file, getmtime(join(directory_path, file))) for file in os.listdir(directory_path)]

# Sort the list of files by modification time
sorted_files = sorted(files, key=lambda x: x[1])

# Rename and add a number prefix to the file names while removing "old_"
for index, (file, mtime) in enumerate(sorted_files, start=1):
    # Remove "old_" from the filename if it exists
    new_file_name = file.replace("-www.w3schools.com", "")
    
    # Add a number prefix
    if "(" in new_file_name:
        pass
    else:
        new_file_name = f"({index}) {new_file_name}"
    
    # Construct the full old and new paths
    old_path = join(directory_path, file)
    new_path = join(directory_path, new_file_name)
    
    # Rename the file
    os.rename(old_path, new_path)

# Print or process the renamed files
for file, mtime in sorted_files:
    print(f"Renamed: {file} -> {new_file_name}")
