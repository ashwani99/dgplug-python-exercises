from bs4 import BeautifulSoup
import requests

def get_links_from_url(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    # Extract the links from anchor tags and make a list
    links = [link.get('href') for link in soup.find_all('a')]
    
    return links
    

get_links_from_url('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')