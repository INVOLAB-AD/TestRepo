#it reads the json file and print the data
import json
str1='{"roll.no":"1","name":"megha"}'
with open("file1.json","a+") as f1:
    f1.write(str1)
                                     

with open("file1.json","r+") as f1:
    str2=f1.read()
    lsf=json.loads(str2)
    for key,value in lsf.items():
        print(key," => ",value)
