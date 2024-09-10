from requests import get
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import img2pdf
from PIL import Image



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


GetUrl = input("링크 주소 입력: ")
driver.implicitly_wait(10)
driver.get(url=GetUrl)


# 문서 로드를 기다리기위한 sleep
time.sleep(5)

iframe = driver.find_element(By.ID,'docFrame')
iframeSrc = iframe.get_attribute("src")
if iframeSrc:
    #새탭 열고 iframe 링크로 이동
    driver.switch_to.new_window('tab')
    driver.get(iframeSrc)
    #이미지 태그 찾기
    img = driver.find_element(By.ID, 'page0')
    imgSrc = img.get_attribute("src")
    print(imgSrc)
    print(type(imgSrc))
    #링크 생성을 위한 전처리
    global_link = imgSrc[:-5]
    print(global_link)
    
    n = 1
    print("----------링크 생성 및 다운로드시작------------")
    while 1:
        link = global_link + str(n) + '.png'
        try:
            urllib.request.urlretrieve(link, "download/" + str(n) + ".png")
            print(link)
            n=n+1
        except:
            print("----------링크 생성 및 다운로드 종료-----------")
            break 

    print("--------png 알파값 처리 시작---------")
    path = r"C:\Users\HomePC\Desktop\scrap\download"
    png_list= os.listdir(path)
    print(png_list)
    i = 1
    png_list_2 = []
    for img in png_list:
        img = Image.open("download/"+str(i)+".png").convert("RGB")
        img.save("download/"+str(i)+".png")
        png_list_2.append("download/"+str(i)+".png")
        i=i+1
    print("-----------png 알파값 처리 완료--------------")
    
    print(png_list_2)

    pdf_name = input("저장할 자료 이름 입력: ")
    print("----------pdf 저장 시작-----------")
    with open(pdf_name + ".pdf", "wb") as file:
        file.write(img2pdf.convert(png_list_2))
    print("----------pdf 저장 완료-----------")


else:
    print('iframe 연결 실패')