import re
import os.path

path = os.getcwd()
fileiist = os.listdir(f"{path}/원본")

for i in fileiist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    ReadFile2 = open(f"{path}/번역본/{i}", 'r' , encoding='UTF-16')
    WriteFile = open(f"{path}/1차 결과물/{i}", 'w', encoding='UTF-8')
    lines = ReadFile.readlines()

    r = re.compile('.*[ぁ-ゔァ-ヴー々〆〤].*$')
    for j in lines:
        aaa = ReadFile2.readline().strip("\n")
        contents = re.sub(r, aaa, j)
        WriteFile.write(contents)
WriteFile.close()