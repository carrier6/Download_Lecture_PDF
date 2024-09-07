import requests
from bs4 import BeautifulSoup

url = 'https://ecampus.changwon.ac.kr/local/ubdoc/?id=311364&tp=m&pg=ubfile'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
