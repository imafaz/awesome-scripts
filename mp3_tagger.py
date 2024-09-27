import os
from mutagen.easyid3 import EasyID3
import re

# Define the directory path where the mp3 files are located
folder_path = 'yas'

# Set the artist and album name
artist = 'yas'
album = 'none'

# Loop through all the files in the specified directory
for file_name in os.listdir(folder_path):

    # Check if the file is an mp3 file
    if file_name.endswith(".mp3"):
        
        # Extract the track name from the file name (without the .mp3 extension)
        track_name = re.sub(r"\.mp3", "", file_name)

        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        try:
            # Load the ID3 information using the mutagen.easyid3 library
            audio = EasyID3(file_path)

            # Update the ID3 tags with the track name, artist, and album information
            audio['title'] = track_name
            audio['artist'] = artist
            audio['album'] = album

            # Save the changes to the file
            audio.save()

        except:
            # If an error occurs, print a message indicating which file could not be processed
            print(f"Could not process file: {file_name}") 