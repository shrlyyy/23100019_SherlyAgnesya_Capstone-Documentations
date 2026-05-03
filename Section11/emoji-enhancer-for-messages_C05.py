'''
Challenge 05: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
    I love to code and drink tea when I'm happy.

Output:
    I love 💖 to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy").
- Handle punctuation (like commas or periods right after keywords).
'''

# Get a dictionary. Bikin dictionary untuk mapping kata dengan emoji yang cocok.
emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍱",
    "pudding": "🍮",
    "games": "🎮",
    "cat": "🐱"
}

# Get user message.
message = input("Enter your message: ")

updated_words = []

# Process each word.
for word in message.split():
    cleaned = word.lower().strip(".,!?-~") # Ini untuk membuat input jadi case-insensitive, lalu strip untuk membersihkan kata yang mempunyai tanda baca yang di dalam kurung karena kalau dipakai tanda baca, nanti kata-katanya tidak bisa cocok dengan emoji yang ada. Nanti baru di-append ke word yang asli.
    emoji = emoji_map_fun.get(cleaned, "") # Kalau tidak ada emojinya, get akan memberikan hasil kosong.

    if emoji:
        updated_words.append(f"{word}{emoji} ") # Ini gabungkan word dengan emoji yang ada.
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("\nEnhanced Message:")
print(updated_message)