print('''                                
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
                                
                           ''')
alphabet = [chr(i) for i in range(97,123)]


def encrypt(message,num):
    caesar_text = ''

    for i in range(len(message)):
        shift_pos = alphabet.index(message[i])+shift_num
        shift_pos %= len(alphabet)
        caesar_text += alphabet[shift_pos]
        
    print("The encrypted message is ",caesar_text)
    return caesar_text

def decrypt(message,num):
    decrypt_mess = ''
    for i in range(len(message)):
        shift_pos = alphabet.index(message[i]) - shift_num
        decrypt_mess += alphabet[shift_pos]

    print("The decrypted message is",decrypt_mess)

method = input("Type 'encode' for encrypt and 'decode' for decrypt\n")
input_message = input("type your message\n")
shift_num = int(input("Type the shift numbers"))

print(len(alphabet))


result = encrypt(input_message,shift_num)
decrypt(result,shift_num)