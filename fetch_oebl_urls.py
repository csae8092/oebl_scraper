import requests
import string
from bs4 import BeautifulSoup
from tqdm import tqdm

from config import OEBL_BASE_URL

lc_letters = string.ascii_lowercase

with open('page_urls.txt', 'w') as f:
    for x in tqdm(lc_letters, total=len(lc_letters)):
        url = f"{OEBL_BASE_URL}{x}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        filter_string = f'/oebl/oebl_{x.upper()}_'
        urls = [x.get('href') for x in soup.find_all("a") if filter_string in x.get('href')]
        for u in urls:
            r = requests.get(OEBL_BASE_URL.replace('/oebl/oebl_', u))
            soup = BeautifulSoup(r.text, 'html.parser')
            for final_url in soup.find_all("a"):
                if '.xml' in final_url.get('href'):
                    f.write(f"{final_url.get('href')}\n")
