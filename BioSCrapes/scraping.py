import requests
from bs4 import BeautifulSoup
import os
import tarfile
import time

def download_and_extract_tar_gz(file_url, folder_name):
    response = requests.get(file_url, stream=True)
    response.raise_for_status()

    # Ensure that the filename is correctly parsed
    filename = file_url.split('/')[-1]
    if not filename:  # If no filename, skip this file
        print(f"Invalid file URL: {file_url}")
        return

    # Define the path to save the downloaded file temporarily
    temp_path = os.path.join(folder_name, filename)
    with open(temp_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    
    # Extract the tar.gz file
    with tarfile.open(temp_path, 'r:gz') as tar:
        tar.extractall(path=folder_name)
        print(f"Extracted {filename} in {folder_name}")

    # Optionally, remove the tar.gz file after extraction if no longer needed
    os.remove(temp_path)
    print(f"Removed temporary file {temp_path}")

def extract_all_files(folder_name, url="https://popo.jpl.nasa.gov/avng/y23_bioscape/"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created directory {folder_name}")

    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        file_url = link.get('href')
        if file_url and file_url.endswith(".tar.gz"):
            full_url = requests.compat.urljoin(url, file_url)
            download_and_extract_tar_gz(full_url, folder_name)



# URL of the webpage containing the files
download_folder = 'BioSCape_Imagery'  # Specify your desired download folder here
#extract_all_files(download_folder)

def download_and_extract_tar_gz(file_url, folder_name, retries=3):
    for attempt in range(retries):
        try:
            start_time = time.time()
            print(f"Starting download: {file_url}")
            response = requests.get(file_url, stream=True, timeout=1800)
            response.raise_for_status()

            filename = file_url.split('/')[-1]
            if not filename:  # If no filename, skip this file
                print(f"Invalid file URL: {file_url}")
                return

            temp_path = os.path.join(folder_name, filename)
            with open(temp_path, 'wb') as file:
                total_size = int(response.headers.get('content-length', 0))
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                print(f"Downloaded {filename} ({total_size} bytes)")

            with tarfile.open(temp_path, 'r:gz') as tar:
                tar.extractall(path=folder_name)
                print(f"Extracted {filename} in {folder_name}")

            os.remove(temp_path)
            print(f"Removed temporary file {temp_path}")
            end_time = time.time()
            print(f"Completed {filename} in {end_time - start_time:.2f} seconds")
            break  # Exit the retry loop on success
        except (requests.exceptions.RequestException, tarfile.TarError) as e:
            print(f"Error during attempt {attempt + 1} for {file_url}: {e}")
            if attempt == retries - 1:
                print(f"Failed to download {file_url} after {retries} attempts")
            else:
                print("Retrying...")


def extract_specific_files(folder_name, filenames, url="https://popo.jpl.nasa.gov/avng/y23_bioscape/"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created directory {folder_name}")

    response = requests.get(url, timeout=1800)
    response.raise_for_status()  # Ensure the request was successful

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        file_url = link.get('href')
        if file_url and any(filename in file_url for filename in filenames):
            full_url = requests.compat.urljoin(url, file_url)
            print(f"Found file: {file_url}")
            download_and_extract_tar_gz(full_url, folder_name)

# URL of the webpage containing the files
download_folder = 'scraped_imagery'  # Specify your desired download folder here
specific_filenames = [
    'ang20231109t064755_011_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t064755_012_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t064755_013_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t064755_014_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t064755_015_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t065855_011_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t065855_012_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t065855_013_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t065855_014_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t071216_012_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t071216_013_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t071216_014_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t071216_015_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t072333_009_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t072333_010_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t072333_011_L2A_OE_main_27577724_RFL_ORT.tar.gz',
    'ang20231109t072333_012_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t072333_013_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t073859_010_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t073859_011_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t073859_012_L2A_OE_main_27577724_RFL_ORT.tar.gz', 
    'ang20231109t073859_013_L2A_OE_main_27577724_RFL_ORT.tar.gz'
]

extract_specific_files(download_folder, specific_filenames)
