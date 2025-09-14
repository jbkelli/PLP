import os
import requests
from urllib.parse import urlparse

def fetch_image():
    url = input("Enter the image URL: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Extract filename from URL or generate one
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        filename = "downloaded_image.jpg"
    save_path = os.path.join(save_dir, filename)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Check if content-type is image
        if 'image' not in response.headers.get('Content-Type', ''):
            print("URL does not point to an image.")
            return
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image: {e}")

if __name__ == "__main__":
    fetch_image()
