import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re


def update_top100():
    
    url = "https://www.billboard.com/charts/hot-100"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    
    titles_gross = soup.select("span.chart-element__information__song")
    titles = []
    for i in titles_gross:
        titles.append(i.get_text())
        
    artists_gross = soup.select("span.chart-element__information__artist")
    artists = []
    for i in artists_gross:
        artists.append(i.get_text())
        
    top100 = pd.DataFrame({'Song':titles,'Artist':artists})
    top100.to_csv('../data/top100songs.csv',index=False)
    return
