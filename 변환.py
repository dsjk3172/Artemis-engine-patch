import re
import os.path

path = os.getcwd()
fileiist = os.listdir(f"{path}/원본")

for i in fileiist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    ReadFile2 = open(f"{path}/번역본/{i}", 'r' , encoding='UTF-16')
    WriteFile = open(f"{path}/최종결과물/{i}", 'w', encoding='UTF-8')
    lines = ReadFile.readlines()

    for j in lines:
        aaa = ReadFile2.readline().strip("\n")
        #aaa = ReadFile2.readline()
        if(aaa == ''):
            WriteFile.write(j)
        else:
            WriteFile.write(aaa)
WriteFile.close()