from PIL import Image
import os
import img2pdf
path = r"C:\Users\HomePC\Desktop\scrap\download\1.png"
print(os.getcwd())
os.path.exists(path)

file_path = r"C:\Users\HomePC\Desktop\scrap\download\1.png"
if os.path.exists(file_path):
    print("파일이 존재합니다.")
else:
    print("파일이 존재하지 않습니다.")

n=4
img = Image.open("download/"+str(n)+".png").convert("RGB")


img.save(r"C:\Users\HomePC\Desktop\scrap\download\44.png")
print("완료")
list = [r"C:\Users\HomePC\Desktop\scrap\download\22.png", r"C:\Users\HomePC\Desktop\scrap\download\44.png"]

print(list)
with open("test.pdf", "wb") as file:
        file.write(img2pdf.convert(list))

'''
png_list= os.listdir(path)
for img in png_list:
    img = Image.open(img)  # 이 부분이 꼭 필요함

    # 알파 채널 제거 (배경을 흰색으로 설정)
    img = Image.new("RGB", img.size, (255, 255, 255))
    img.paste(img, mask=img.split()[3])  # 알파 채널에 대한 투명도 처리

    # 알파 채널이 없는 이미지로 저장
    img.save()
    print("완료")
    '''