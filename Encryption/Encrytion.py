def encrypter():
    pass


def decrpter():
    pass


# Driver Code
line = input("Enter string to encrypt: ")
alphas = ["a","b","c","d","e","f","g","h"]
code = ["w","e","f","q","r","s","t","p"]
coded=[]

for char in line:
    index = alphas.index(char)
    coded.append(index)

codedline=[]
for num in coded:
    codedline.append(code[num])

codedline = ''.join(codedline)

print(codedline)



