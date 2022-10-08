import requests
import os
from bs4 import BeautifulSoup

from config import OEBL_BASE_URL


with open("page_urls.txt") as f:
    for index, line in enumerate(f):
        url = line.strip()
        print(url)
        start_date = url.split("_")[-2]
        folder = url.split("/")[2]
        os.makedirs(f"./data/{folder}", exist_ok=True)
        fetch_url = OEBL_BASE_URL.replace("/oebl/oebl_", url)
        f_name = fetch_url.split("/")[-1].replace('.xml', '.html')
        r = requests.get(fetch_url)
        soup = BeautifulSoup(r.content.decode("utf-8"), "html.parser")
        with open(f"./data/{folder}/{f_name}", "w") as out_file:
            out_file.write(str(soup))
