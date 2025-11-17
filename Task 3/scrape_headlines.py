import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"Attempting to fetch headlines from: {URL}\n")

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status() 

    soup = BeautifulSoup(response.content, 'html.parser')

    all_links = soup.find_all('a')

    headline_texts = set()
    
    for link in all_links:
        text = link.get_text(strip=True)
        href = link.get('href')

        if not href:
            continue
            
        if len(text) < 20:
            continue

        if href.startswith('/news/') :
            headline_texts.add(text)

    if headline_texts:
        sorted_headlines = sorted(headline_texts)
        
        print("Found headlines:\n" + "-"*30)
        for i, text in enumerate(sorted_headlines, start=1):
             print(f"{i}. {text}")
             
        with open('headlines.txt', 'w', encoding='utf-8') as f:
            for i, line in enumerate(sorted_headlines, start=1):
                f.write(f"{i}. {line}\n")
        
        print("\n" + "-"*30)
        print(f"\nSuccess! Saved {len(sorted_headlines)} numbered headlines to headlines.txt")
    
    else:
        print("\n" + "-"*30)
        print("\nFailed. ")


except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")