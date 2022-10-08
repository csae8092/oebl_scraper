import pandas as pd
import glob
import os
import re
from bs4 import BeautifulSoup
from tqdm import tqdm


files = sorted(glob.glob("./data/**/*.html"))
data = []
for x in tqdm(files, total=len(files)):
    _, tail = os.path.split(x)
    if "Verweis" in tail:
        continue
    item = {}
    try:
        item["start"], item["end"] = re.findall(r"\d+", tail)
    except:
        item["start"], item["end"] = re.findall(r"\d+", tail), "0000"
    item["f_name"] = tail
    item["gnd"] = None
    item["doi"] = None
    item["name"] = None
    try:
        with open(x, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
            item["name"] = soup.find("meta", {"name": "DC.Title"}).get("content")
            for x in soup.find("div", {"id": "docNavi2"}).findChildren("a"):
                href = x.get("href")
                if "d-nb.info" in href:
                    item["gnd"] = href
                if "//doi.org/" in href:
                    item["doi"] = href
    except Exception as e:
        print(x, e)
        continue

    data.append(item)

df = pd.DataFrame
df.to_csv("info.csv", index=False)
