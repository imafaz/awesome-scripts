import threading
import os
import requests
from urllib.parse import unquote

def download(url, conections , filepath='.'):
    try:
        response = requests.head(url, allow_redirects=True)
        file_size = int(response.headers['Content-Length'])
        file_name = os.path.basename(unquote(response.url))
        lock = threading.Lock()
        print(f"File name: {file_name}")
        print(f"File size: {file_size/(1024*1024):.2f} MB")
        print(f"File link: {response.url}")
        filepath = os.path.join(filepath, file_name)

        if os.path.exists(filepath):
            print(f"{file_name} already exists, skipping...")
            return

        part_size = file_size // conections

        def download_part(start, end, i):
            headers = {'Range': 'bytes={}-{}'.format(start, end)}
            res = requests.get(url, headers=headers)

            with open(f'{filepath}.part{i}', 'wb') as f:
                f.write(res.content)

            with lock:
                print(f"Connection {i}: {file_name}.part{i} ({len(res.content)/(1024*1024):.2f}MB) downloaded.")

        threads = []
        for i in range(conections):
            start = i*part_size
            end = start + part_size - 1
            if i == conections-1:
                end = file_size - 1

            thread = threading.Thread(target=download_part, args=(start, end, i))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        with open(filepath, 'wb') as f:
            for i in range(conections):
                with open(f'{filepath}.part{i}', 'rb') as fr:
                    f.write(fr.read())
                os.remove(f'{filepath}.part{i}')

        print(f"{file_name} downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")