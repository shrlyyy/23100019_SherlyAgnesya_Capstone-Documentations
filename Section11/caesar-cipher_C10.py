'''
Challenge 10: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using a simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
    - Ask for a message and a numeric secret key.
    - Use a Caesar Cipher (shift letters by the key value).
    - Output the encrypted message.
3. If decrypting:
    - Ask for the encrypted message and key.
    - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 -> 'a').

Bonus:
- Allow uppercase and lowercase letter handling.
- Show a clean interface.
'''

def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') # "ord" itu ubah karakter jadi angka (kode ASCII/Unicode). "chr" itu kebalikannya.
            shifted = (ord(char) - base + key) % 26 + base # Kurangi dengan base agar angkanya jadi 0-25, key itu kunci rahasia cipher-nya, modulo untuk wrap around kembali ke A lagi kalau ada di Z, tambahkan dengan base agar kembali ke angka ASCII.
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)

print("Secret Message Program")
choice = input("Do you want to E or D? ").strip().lower()

if choice == "e":
    text = input("Enter your message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        encrypted = encrypt(text, key)
        print("Encrypted message: ")
        print(encrypted)
    except ValueError:
        print("Invalid Key.")
elif choice == 'd':
    text = input("Enter your encrypted message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        decrypted = decrypt(text, key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError:
        print("Invalid Key.")
else:
    print("Invalid Choice.")