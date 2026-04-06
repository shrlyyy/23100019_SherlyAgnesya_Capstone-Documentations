'''
MINI PROJECT 11
You're preparing an order summary with customer names
and their total bill.

Task:
- Use two lists: one for names and one for bills.
- Print: "[Name] paid $[amount]"
'''

names = ["Haru", "Kenma", "Yushi", "Kozu"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} dollars")