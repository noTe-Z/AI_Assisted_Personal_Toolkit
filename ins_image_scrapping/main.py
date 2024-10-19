import json
import os
import requests
from urllib.parse import urlparse

def extract_urls_from_log(log_file):
    with open(log_file, 'r') as f:
        log_data = json.load(f)
    
    image_urls = set()
    for entry in log_data['log']['entries']:
        if 'request' in entry:
            url = entry['request']['url']
            if 'instagram.com' in url and any(ext in url for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                image_urls.add(url)
    
    return list(image_urls)

def download_images(urls, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = os.path.join(folder, os.path.basename(urlparse(url).path))
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {url}")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

def main():
    log_file = '/Users/chenyuan/Development/ai_copilot_development/ins_image_scrapping/www.instagram.com.har'
    download_folder = './downloaded_images'
    
    urls = extract_urls_from_log(log_file)
    print(f"Found {len(urls)} image URLs")
    
    download_images(urls, download_folder)
    print("Download complete!")

if __name__ == "__main__":
    main()