message=input('enter the message:')
alphabet='abcdefghijklmnopqrstuvwxyz'
key=5
encrypt=''
for i in message:
    position=alphabet.find(i)
    newposition=(position+5)%26
    encrypt+=alphabet[newposition]

print(encrypt)
