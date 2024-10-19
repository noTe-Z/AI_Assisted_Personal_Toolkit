import requests
from bs4 import BeautifulSoup
import csv
import time

def get_paper_details(paper_url):
    response = requests.get(paper_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    abstract = soup.find('div', id='abstract').text.strip()
    
    related_material = []
    material_section = soup.find('div', id='related_material')
    if material_section:
        links = material_section.find_all('a')
        for link in links:
            related_material.append(link.text.strip())
    
    return abstract, ', '.join(related_material)

# URL of the paper list webpage
url = "https://openaccess.thecvf.com/CVPR2024?day=all"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all paper entries
paper_entries = soup.find_all('dt', class_='ptitle')

# Prepare CSV file
with open('cvpr2024_papers_detailed.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Paper Title', 'Authors', 'PDF Link', 'Abstract', 'Related Material'])

    # Extract information for each paper
    for entry in paper_entries:
        # Extract paper title and link
        title_link = entry.find('a')
        title = title_link.text.strip()
        paper_detail_url = "https://openaccess.thecvf.com/" + title_link['href']

        # Find the next 'dd' tag for authors
        authors_tag = entry.find_next('dd')
        authors = authors_tag.text.strip() if authors_tag else "N/A"

        # Find the PDF link
        pdf_link_tag = entry.find_next('a', text='pdf')
        pdf_link = "https://openaccess.thecvf.com/" + pdf_link_tag['href'] if pdf_link_tag else "N/A"

        # Get paper details
        abstract, related_material = get_paper_details(paper_detail_url)

        # Write to CSV
        csvwriter.writerow([title, authors, pdf_link, abstract, related_material])

        # Add a small delay to avoid overwhelming the server
        time.sleep(1)

print("Data has been extracted and saved to cvpr2024_papers_detailed.csv")