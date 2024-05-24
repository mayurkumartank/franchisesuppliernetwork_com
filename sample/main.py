import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def analysis(img_urls, link_urls, output_folder):
    filtered_urls = [url for url in img_urls if url.endswith('.png') or url.endswith('.jpg') or url.endswith('.jpeg')]
    image_download(filtered_urls,output_folder)
    
    img_count = png_count = jpg_count = jpeg_count = 0
    for url in img_urls:
        if url.endswith(('.png', '.jpg', '.jpeg')):
            img_count += 1
            if url.endswith('.png'):
                png_count += 1
            elif url.endswith('.jpg'):
                jpg_count += 1
            elif url.endswith('.jpeg'):
                jpeg_count += 1
                
    domain = output_folder.split("\\")[1].replace("_",".")      
    with open(os.path.join(output_folder, 'analysis.txt'), 'w') as f:
        f.write(f"Domain: {domain}\n\n")
        f.write(f"1. Images count: {img_count}\n")
        f.write(f"      * png count: {png_count}\n")
        f.write(f"      * jpg count: {jpg_count}\n")
        f.write(f"      * jpeg count: {jpeg_count}\n\n")
        f.write(f"2. Links count: {len(link_urls)}\n")
        
def image_download(img_urls,output_folder):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    output_folder = os.path.join(output_folder, 'images')
   
    for img_url in img_urls:
        img_response = requests.get(img_url, headers=headers)
        if img_response.status_code == 200:
            img_filename = os.path.basename(img_url)
            extension = img_filename.split('.')[-1].lower() 
            
            img_filepath = os.path.join(output_folder,extension,img_filename)
            os.makedirs(os.path.dirname(img_filepath), exist_ok=True)

            with open(img_filepath, 'wb') as img_file:
                img_file.write(img_response.content)
            
def extract_content(html_content,output_folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    content = []
    img_urls = []
    link_urls = []
    for tag in soup.find_all(['img', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']):
        if tag.name == 'img':
            img_url = tag['src']
            if img_url not in img_urls:  
                img_urls.append(img_url)
                content.append(img_url)
                
        elif tag.name == 'a':
            link_url = tag.get('href') or tag.get('src', '')
            link_text = tag.get_text(strip=True)
            link_urls.append(link_url)
            if link_text and link_url:
                content.append(f"{link_text} - {link_url}")
        else:
            text = tag.get_text(strip=True)
            if text not in content:
                content.append(text)
                
    analysis(img_urls,link_urls,output_folder)
    return content

def write_to_txt(content, output_folder):
    with open(output_folder, 'w', encoding='utf-8') as f:
        for item in content:
            f.write(str(item) + '\n')

def main():
    url = 'https://franchisesuppliernetwork.com'
    domain = urlparse(url).netloc.replace(".","_")
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        output_folder = os.path.join('output folder', domain)
        os.makedirs(output_folder, exist_ok=True)
            
        content = extract_content(response.text,output_folder)
        output_folder = os.path.join(output_folder, 'output_main.txt')
        write_to_txt(content,output_folder)

if __name__ == "__main__":
    main()