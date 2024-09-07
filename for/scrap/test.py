import requests

# 요청을 보내서 HTML 가져오기
url = "https://ecampus.changwon.ac.kr/mod/ubfile/view.php?id=311364"
response = requests.get(url)

# HTML을 파일로 저장
with open("page.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML 파일이 저장되었습니다.")