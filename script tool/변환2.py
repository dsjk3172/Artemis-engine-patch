import re
import os.path

path = os.getcwd()
fileiist = os.listdir(f"{path}/1차 결과물")

for i in fileiist:
    ReadFile = open(f"{path}/1차 결과물/{i}", 'r' , encoding='UTF-8')
    ReadFile2 = open(f"{path}/시스템 문장 추출본/{i}", 'r' , encoding='UTF-8')
    WriteFile = open(f"{path}/최종 결과물/{i}", 'w', encoding='UTF-8')
    lines = ReadFile.readlines()

    a = 0

    r = re.compile('.*[a-zA-Z].*$')
    p = re.compile('name = ')
    m = re.compile('"rt2"')
    for j in lines:
        aaa = ReadFile2.readline().strip("\n")
        if(a == 0):
            contents = re.sub(r, aaa, j)
        if p.search(aaa):
            a = a + 1
        elif(a != 0):
            contents = j
        if m.search(aaa):
            a = 0
        WriteFile.write(contents)
WriteFile.close()