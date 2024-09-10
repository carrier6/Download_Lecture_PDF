import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import img2pdf
from PIL import Image
from glob import glob
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


#download 폴더 초기화
reset_dir = glob('download/*.png')
for r in reset_dir:
    os.remove(r)

GetUrl = input("링크 주소 입력: ")
driver.implicitly_wait(10)
driver.get(url=GetUrl)


time.sleep(5)

iframe = driver.find_element(By.ID,'docFrame')
iframeSrc = iframe.get_attribute("src")
if iframeSrc:
    #새탭 열고 iframe 링크로 이동
    driver.switch_to.new_window('tab')
    driver.get(iframeSrc)
    time.sleep(5)
    #이중iframe 링크 이동
    Second_iframe = driver.find_element(By.ID,'innerWrap')
    Second_iframeSrc = Second_iframe.get_attribute("src")
    driver.set_window_size(1480, 920) #1280:720 화면비 +200
    driver.get(Second_iframeSrc)
    global_link = Second_iframeSrc[:-7]
    print(global_link)
    
    #페이지가 0부터 인덱싱되있으므로 n=0
    n = 0
    print("----------링크 생성 및 다운로드시작------------")
    while 1:
        #n이 10을 넘어갈 시 글로벌 링크 수정(최대 100페이지 다운로드 가능, n>99조건 추가시 최대 1000페이지 다운로드 가능)
        if n > 9:
            global_link = Second_iframeSrc[:-8]
        link = global_link + str(n) + '.xhtml'
        
        try:
            # 링크 접속
            driver.get(link)
            driver.implicitly_wait(10)
            #sng 태그 선택 및 스크린샷
            svg = driver.find_element(By.TAG_NAME, "svg:svg")
            svg.screenshot("download/"+str(n)+".png")
            print(link)
            n=n+1
        except:
            print("----------링크 생성 및 다운로드 종료-----------")
            break

    print("--------png 알파값 처리 시작---------")
    path = r"C:\Users\HomePC\Desktop\scrap\download"
    png_total = len(glob('download/*.png'))
    #png_list= os.listdir(path)
    print(str(png_total)+"개 완료")
    i = 0
    png_list = []
    for f in range(png_total):
        img = Image.open("download/"+str(i)+".png").convert("RGB")
        img.save("download/"+str(i)+".png")
        png_list.append("download/"+str(i)+".png")
        i=i+1
    print("-----------png 알파값 처리 완료--------------")

    print(png_list)

    pdf_name = input("저장할 자료 이름 입력: ")
    print("----------pdf 저장 시작-----------")
    with open(pdf_name + ".pdf", "wb") as file:
        file.write(img2pdf.convert(png_list))
    print("----------pdf 저장 완료-----------")


else:
    print('iframe 연결 실패')