alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
          ,'r','s','t','u','v','w','x','y','z']


def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text+=char

    print(f"here is the text after the encryption {cipher_text}")


    
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    
    
        

    print(f"here is the text after decrypton {plain_text}")


nikhil=True
while nikhil:
    what_to_do=input("type 'encrypt' for encryption , type 'decrypt' for decryption: ")
    text=input("enter your message: ")
    shift=int(input("enter shift key: "))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    else:
        print("type a valid choice given between")
    chooser=input("if you want to continue type yes or discontinue type no: ")
    if chooser=="yes":
        nikhil=True
    elif chooser=="no":
        nikhil=False
    else:
        nikhil=False

