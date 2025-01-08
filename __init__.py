from curl_cffi import requests
from bs4 import BeautifulSoup

def scrape(query):
    raw = requests.get("https://duckduckgo.com/html/?q=" + query, impersonate="chrome")
    soup = BeautifulSoup(raw.text, 'html.parser')

    results = soup.find_all('div', class_='result results_links results_links_deep web-result')

    scraped_data = []

    for result in results:
        title_element = result.find('h2', class_='result__title')
        title = title_element.a.text.strip() if title_element else ''
        
        url_element = result.find('a', class_='result__url')
        url = url_element.text.strip() if url_element else ''
        
        snippet_element = result.find('a', class_='result__snippet')
        snippet = snippet_element.text.strip() if snippet_element else ''
        
        date_element = result.find('span', string=lambda text: text and '-' in text)
        date = date_element.text.strip() if date_element else ''
        
        result_data = {
            'title': title,
            'url': url,
            'description': snippet,
            'date': date
        }
        
        scraped_data.append(result_data)
        return scraped_data