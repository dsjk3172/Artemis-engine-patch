import re
import os.path

path = os.getcwd()
filelist = os.listdir(f"{path}/원본")

for i in filelist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    writefile = open(f"{path}/일본어 추출본/{i}", 'w', encoding='UTF-8')
    readline = ReadFile.readlines()

    abc = list()

    r = re.compile('.*[ぁ-ゔァ-ヴー々〆〤].*$')
    for i in readline:
        abc = re.findall(r, i)
        contents = "".join(abc) + "\n"
        writefile.write(contents)
    writefile.close()