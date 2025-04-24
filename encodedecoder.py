import os

key="x0x0x"
data=open('./encoder/data.txt', 'r').read()
encChar=""
for i in range(len(data)):
    char=data[i]
    dynamicKey=key[i%len(key)]
    encChar+=chr(ord(char)^ord(dynamicKey))
    
file = open('./encoder/data.txt', 'w')
file.write(encChar)