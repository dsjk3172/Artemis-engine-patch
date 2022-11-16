import re
import os.path

path = os.getcwd()
filelist = os.listdir(f"{path}/원본")

for i in filelist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    writefile = open(f"{path}/추출본/{i}", 'w', encoding='UTF-8')
    readline = ReadFile.readlines()

    abc = list()

    r = re.compile('.*[a-z].*$')
    for i in readline:
        #abc = re.findall(r, i)
        abc = re.sub(r, '', i)
        contents = "".join(abc) + "\n"
        writefile.write(contents)
    writefile.close()