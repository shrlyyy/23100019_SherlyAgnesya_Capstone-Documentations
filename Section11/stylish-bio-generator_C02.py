'''
Challenge 02: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
    - Name
    - Profession
    - One-liner passion or goal
    - Favorite emoji (optional)
    - Website or handle (optional)

2. Generate a stylish 2-3 lines using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
    Name: Riya
    Profession: Designer
    Passion: Making things beautiful
    Emoji: 🎨
    Website: @riya.design

Output:
    🎨 Riya | Designer
    💡 Making things beautiful
    🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a '.txt' file.
'''

import textwrap # Untuk atur text di output.

# Input dari User.
name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple Lines ")
print("2. Vertical Flair ")
print("3. Emoji Sandwich")

style = input("Enter 1, 2, or 3: ").strip()

# Untuk bikin 3 style pilihan.
def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name} \n{profession}🔥 \n{passion} \n{website}🔥"
    elif style == "3":
        return f"{emoji*3} \n{name} - {profession} \n{passion} \n{website} \n{emoji*3}"
    
bio = generate_bio(style)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio)) # Dedent berguna untuk string yang punya spasi di awal baris, auto rata kiri waktu print.
print("*" * 50)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()

# File handling
if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f: # Kalau pakai with, Pyhton langsung tutup file setelah selesai. Utf-8 karena ada pakai emoji.
        f.write(bio)
    print("File saved!")
