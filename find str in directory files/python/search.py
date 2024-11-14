import os

def search_in_file(file_path, search_word):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        file_content = file.read()
        if search_word.lower() in file_content.lower():
            print(f"Found in: {file_path}")

def recursive_search(directory, search_word):
    for item in os.listdir(directory):
        if item == '.' or item == '..':
            continue

        file_path = os.path.join(directory, item)
        if os.path.isdir(file_path):
            recursive_search(file_path, search_word)
        else:
            search_in_file(file_path, search_word)

directory_path = input("Please enter directory name: ")
search_word = input("Please enter word to search: ")

recursive_search(directory_path, search_word)
