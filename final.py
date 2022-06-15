def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

def cipher_encryption(message):
    # message = input("Enter message: ")
    key = 47
    encryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)
        # if-else
    # for
    
    j = '\n'.join(encryp_text.split('9'))

    with open('encrypted.txt', 'w') as f:
        f.write(j)
                
        # f.write(decryp_text)
    print("Encrypted Text: {}".format(j))
    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
     
