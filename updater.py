import requests
import os
import glob
import shutil
import sys

def is_running_as_exe():
    # Checks if the script is running as a compiled executable
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

def find_obsidian_executable(directory):
    search_pattern = os.path.join(directory, "Obsidian*.exe")
    found_files = glob.glob(search_pattern)
    if not found_files:
        print("No Obsidian executable found in script's directory.")
        return None
    return found_files[0]

def get_versioned_filename(latest_release):
    version = latest_release['tag_name'].lstrip('v')  # Remove 'v' from version string
    return f"Obsidian.{version}.exe"

def get_version(filename):
    # Assuming the version is in the filename in the format 'Obsidian.X.X.X.exe'
    return filename.split('Obsidian.')[1].split('.exe')[0]

def is_latest_release(latest_release, local_exe_path):
    latest_release_version = get_version(latest_release)
    local_exe_version = get_version(os.path.basename(local_exe_path))

    return latest_release_version != local_exe_version

def download_latest_obsidian(releases_url, local_exe_path, directory):
    print("Fetching the latest release from GitHub...")
    response = requests.get(releases_url)
    response.raise_for_status()
    latest_release = response.json()[0]
    print(f"Latest release: {latest_release['tag_name']}")

    # Check if the latest release is the same as the local executable
    if is_latest_release(latest_release, local_exe_path):
        print("The Obsidian executable is already up to date.")
        return

    download_url = latest_release['assets'][0]['browser_download_url']
    print(f"Download URL: {download_url}")

    new_filename = get_versioned_filename(latest_release)
    download_path = os.path.join(directory, new_filename)
    print(f"Downloading and saving as: {new_filename}")

    response = requests.get(download_url)
    with open(download_path, "wb") as file:
        file.write(response.content)

    try:
        print(f"Attempting to replace old executable: {local_exe_path}")
        if os.path.exists(local_exe_path):
            os.remove(local_exe_path)
            print(f"Deleted old executable: {local_exe_path}")
        print("Replacement complete. New version updated.")
    except Exception as e:
        print(f"Error during file replacement: {e}")

releases_url = "https://api.github.com/repos/obsidianmd/obsidian-releases/releases"

# Determine the directory based on how the script is running
if is_running_as_exe():
    directory = os.path.dirname(sys.executable)
else:
    directory = os.path.dirname(os.path.realpath(__file__))

obsidian_exe_path = find_obsidian_executable(directory)

if obsidian_exe_path:
    download_latest_obsidian(releases_url, obsidian_exe_path, directory)
else:
    print("Script did not find any Obsidian executable to update.")
