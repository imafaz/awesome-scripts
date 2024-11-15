import os

def replace_in_file(file_path, search, replace):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    if search in file_content:
        new_content = file_content.replace(search, replace)
        
        if new_content != file_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            return True
    return False

def recursive_search(directory, search, replace):
    modified_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if replace_in_file(file_path, search, replace):
                modified_files.append(file_path)
    
    return modified_files


directory_path = input("Enter the directory path: ")
search_word = input("Enter the word to search: ")
replace_word = input("Enter the word to replace with: ")


if not os.path.isdir(directory_path):
    print("The specified directory does not exist.")
    exit(1)

modified_files = recursive_search(directory_path, search_word, replace_word)

if modified_files:
    print("Replacements were made in the following files:")
    for modified_file in modified_files:
        print(modified_file)
else:
    print("No replacements were made.")
