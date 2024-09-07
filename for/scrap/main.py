import requests
import sys
from bs4 import BeautifulSoup


url = input('url: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
with open("page3.html", "w", encoding="utf-8") as file:
    file.write(.text)

'''
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print('sucess!')
    img = soup.select_one('img#page0')
    print(img)
    imgList=[]
    for src in img:
        if 'src' in src.attrs:
            imgList.append(src.attrs['src'])
    if img:
        print('sucess')
    else:
        print("Tlqkf")
    
'''
# https://ecampus.changwon.ac.kr/mod/ubfile/view.php?id=311364
# https://ecampus.changwon.ac.kr/local/ubdoc/?id=311364&tp=m&pg=ubfile
# https://doc.coursemos.co.kr/changwon/28999/4145ed54019ec388196cf06705e1dc6d51413039/4145ed54019ec388196cf06705e1dc6d51413039.files/1.png