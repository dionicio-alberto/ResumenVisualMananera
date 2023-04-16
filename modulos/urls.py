import requests as rq
import numpy as np
from bs4 import BeautifulSoup

def url_dia():

    url='https://www.gob.mx/presidencia/archivo/articulos?idiom=es&&filter_origin=archive&category=764'
    website_url= rq.get(url)
    soup = BeautifulSoup(website_url.text,'html.parser')

    data = [element.get('href') for element in soup.find_all('a')]

    i,ii=True,0
    while i:
        
        if data[ii][50:55]=='confe':
            url=data[ii][2:-2]
            i=False  
        ii=ii+1

    gobierno='https://www.gob.mx/'
    url_final=gobierno+url
    return(url_final)

if __name__ == '__main__':
    a = url_dia()
    print(a)

