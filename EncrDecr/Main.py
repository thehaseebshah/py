# Driver Code
import binascii
import Enc
import Decr

print()
print()
text = input("Enter text to encrypt: ")
key = input("Enter key: ")
ascii_text = []
ascii_key = []
for i in text:
    ascii_text.append(ord(i))
for i in key:
    ascii_key.append(ord(i))
print(ascii_key)
print(ascii_text)

bin_text = []
bin_key = []
for i in ascii_text:
    bin_text.append(bin(i))
for i in ascii_key:
    bin_key.append(bin(i))

print(bin_key)
print(bin_text)

xored_key = []
j=0
k=1
for i in range((len(bin_key) - 1)):
    xored_key.append(bin(int(bin_key[j],2)^int(bin_key[k],2)))
    j+=1
    k+=1


while len(xored_key) < len(bin_text):
    xored_key.append(bin(0))

print(xored_key)

xored_code = []
j=0
for i in bin_text:
    xored_code.append(bin(int(xored_key[j], 2) ^ int(bin_text[j], 2)))

print("Answer is",xored_key)