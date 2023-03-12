import concurrent.futures
import urllib.request
from time import sleep

URLS = ["http://foxnews.com","http://cnn.com","http://bbc.co.uk", "http://bad.link", "https://hogart.ru"]

def load_url(url, timeout):
    sleep(10)
    with urllib.request.urlopen(url, timeout=timeout ) as conn:
        return conn.read()
    
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = { executor.submit(load_url, url, 60): url for url in URLS } #запуск потоков
    for future in concurrent.futures.as_completed(future_to_url):  
        url = future_to_url[future] 
        try:
            data = future.result()
        except Exception as exc:
            print(f'{url} caused exception: {exc}')
        else: 
            print(f'{url} page is {len(data)} bytes')