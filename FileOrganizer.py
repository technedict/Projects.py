import os
import shutil

def is_hidden(filepath):
    # Function to check if a file or directory is hidden (for Unix-based systems)
    return os.path.basename(filepath).startswith(".")

def list_files_with_extension(directory, file_extension):
    files_with_extension = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not is_hidden(file) and file.lower().endswith(f".{file_extension}"):
                file_path = os.path.join(root, file)
                files_with_extension.append(file_path)
    return files_with_extension

def organize_files_by_extension(source_directory, target_directory, file_extension):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    files_with_extension = list_files_with_extension(source_directory, file_extension.lower())

    for file_path in files_with_extension:
        file_name = os.path.basename(file_path)
        target_file_path = os.path.join(target_directory, file_name)

        if not os.path.exists(target_file_path):
            shutil.move(file_path, target_file_path)
        else:
            base_name, extension = os.path.splitext(file_name)
            i = 1
            while os.path.exists(target_file_path):
                new_file_name = f"{base_name}_{i}{extension}"
                target_file_path = os.path.join(target_directory, new_file_name)
                i += 1
            shutil.move(file_path, target_file_path)

if __name__ == "__main__":
    target_directory = os.path.expanduser("~")
    user_input_extension = input("Enter the file extension you want to search for (e.g., 'txt', 'pdf', 'jpg'): ")
    files_with_extension = list_files_with_extension(target_directory, user_input_extension.lower())

    if not files_with_extension:
        print(f"No files with '{user_input_extension}' extension found in the directory.")
    else:
        print(f"Files with '{user_input_extension}' extension found in the directory:")
        for file_path in files_with_extension:
            print(file_path)

    organize_choice = input("Do you want to organize these files into a new directory? (y/n): ")
    if organize_choice.lower() == "y":
        target_directory = input("Enter the path for the target directory to organize the files: ")
        organize_files_by_extension(target_directory, target_directory, user_input_extension.lower())
        print(f"Files with '{user_input_extension}' extension have been organized into '{target_directory}' directory.")