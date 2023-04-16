import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = ' '.join([t.get_text() for t in soup.find_all('p')])

        return texts
    else:
        raise Exception(f"Failed to fetch the web page: {response.status_code}")
