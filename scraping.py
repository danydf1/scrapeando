from bs4 import BeautifulSoup
import requests

#https://www.youtube.com/watch?v=y7-Zm5wdARU jony devrock

#antes de usar ejecutar "pip install -r requerimientos.txt" 

url = "https://www.lanacion.com.ar"
page= requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

titulos = soup.find_all('h2', "com-title")

for til in titulos:
    sub = til.find_all('a')
    print(sub[0].attrs.get('title'))


