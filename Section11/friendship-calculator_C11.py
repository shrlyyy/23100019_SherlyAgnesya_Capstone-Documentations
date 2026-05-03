'''
Challenge 11: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (1-100).
3. Display the percentage with a themed message like:
    "You're like chai and samosa - made for each other!" or "Well.. opposites attract, maybe?"

Bonus:
    - Use emojis in the result.
    - Give playful advice based on the score range.
    - Capitalize and center the final output in a framed box.
'''

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2) # Untuk cari irisan karakter kata yang ada di 2 nama.
    vowels = set('aiueo')

    score += len(shared_letters) * 15
    score += len(vowels & shared_letters) * 20

    return min(score, 100)

def get_message(score): # Challenge: Bikin themed message.
    if score >= 80:
        return "You're like chai and samosa - made for each other! 🍵🥟", "Best friends forever! 🫂"
    elif score >= 50:
        return "Solid team! 🤜🤛", "Go out and grab some coffee sometime! ☕"
    else:
        return "Well.. opposites attract, maybe? 🌓", "Don't worry, even the most different people can be great friends. 🤝"

def run_friendship_calculator():
    print("💖 Friendship Compatibility Calculator 💖")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)
    message, advice = get_message(score)

    result_txt = f"{name1.upper()} & {name2.upper()}"
    border = "*" * 60
    
    print(f"\n{border}")
    print(result_txt.center(60))
    print(f"{score}".center(60))
    print(f"Message: {message}".center(60))
    print(f"Advice: {advice}".center(60))
    print(border)

run_friendship_calculator()
