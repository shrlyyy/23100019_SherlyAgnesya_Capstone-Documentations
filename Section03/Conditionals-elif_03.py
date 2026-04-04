'''
MINI PROJECT 03
A tea stall offers different prices for different cup sized.
Write a program that calculates the price based on size.

Task:
- Input: "small", "medium", "large".
- Small -> $10, Medium -> $15, Large -> $20.
- If invalid: show "Unknown cup size".
'''

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 dollars")
elif cup == "medium":
    print("Price is 15 dollars.")
elif cup == "large":
    print("Price is 20 dollars.")
else:
    print("Unknown cup size.")