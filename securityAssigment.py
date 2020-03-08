def process(type,operation,input):
    output = ""
    s=4
    a=11
    b=25
    k='key'
    if type=="shift":
        if operation=="encrypt":
            for i in range(len(input)):

                if (input[i].isupper()):
                    output += chr((ord(input[i]) + s - 65) % 26 + 65)
                else:
                    output += chr((ord(input[i]) + s - 97) % 26 + 97)
            return output

        elif operation=="decrypt" :
             for i in range(len(input)):

                 if (input[i].isupper()):
                     output += chr((ord(input[i]) -s - 65) % 26 + 65)
                 else:
                     output += chr((ord(input[i]) - s - 97) % 26 + 97)
             return output

    elif type == "affine":
        if operation=="encrypt":
            for i in range(len(input)):
                if(input[i].islower()): output += chr(((a * ord(input[i].upper())-65)  + b) % 26 + 65)
                else :output += chr(((a * ord(input[i])-65)  + b) % 26 + 65)


            return output
        elif operation == "decrypt":
            a_inv = 0
            for i in range(26):
                if ((a * i) % 26) == 1 :
                        a_inv = i
            for i in range(len(input)):
                    output += chr(((a_inv * (ord(input[i])- b-65)) % 26) + 65)
            return output

    elif type == "vigenere":
            generated_Key = ""
            key_Size = len(k)
            j = 0
            if (key_Size == 0): return input
            for i in range(len(input)):
                if (j >= key_Size):j = 0
                generated_Key += k[j]
                j+=1
            if operation == "encrypt":
                input.upper()
                for i in range(len(input)):
                    if (input[i].islower()): output += chr(((ord(input[i].upper()) - 65) + (ord(generated_Key[i]) - 65)) % 26 + 65)
                    else :output += chr(((ord(input[i]) - 65) + (ord(generated_Key[i]) - 65)) % 26 + 65)
                return output
            elif operation == "decrypt":
                for i in range(len(input)):
                        output += chr(((ord(input[i])-65)-(ord(generated_Key[i])-65)+26)%26+65)
                return output




output =process('vigenere','encrypt','AMIRMSIAM')
print (output)
msg=process('vigenere','decrypt',output)
print(msg)

