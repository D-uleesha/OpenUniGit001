import os
import urllib.request

# URL of the file to fetch
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/330px-GitHub_Invertocat_Logo.svg.png"

# Folder name to save the fetched file
folder_name = "image"

# File name to save
file_name = "image.png"

# Create the 'fetch' folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Full path to save the file
file_path = os.path.join(folder_name, file_name)

try:
    # Fetch the file from the URL and save it
    print(f"Fetching file from: {url}")
    urllib.request.urlretrieve(url, file_path)
    print(f"File saved to: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

