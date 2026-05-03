'''
Challange 08: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters).
2. At least one uppercase letter.
3. At least one lowercase letter.
4. At least one digit.
5. At least one special character (e.g., @, #, $, etc.).

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using 'getpass' (no echo on screen).
'''

import string # Modul semua huruf, angka, tanda baca.
import random # Untuk acak karakter saat bikin generate random password.
import getpass # Modul untuk input user invisible.

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter.")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter.")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit.")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing punctuatuon.")
    return issues

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation # Bikin satu 'kolam' campuran semua huruf (kecil, besar), angka, simbol.
    return "".join(random.choice(chars) for _ in range(length)) # Ambil karakter secara acak dan sebanyak 12 kali seperti yang sudah di-define lalu di-join.

password = getpass.getpass("Enter a password: ") # Ini input user-nya invisible karena pakai getpass.
issues = check_password_strength(password)

if not issues:
    print("Strong password! You are good to go.")
else:
    print("You got weak password.")
    for issue in issues:
        print(f"- {issue}")

suggestion = generate_strong_password()
print("\n Suggesting you a strong password")
print(suggestion)