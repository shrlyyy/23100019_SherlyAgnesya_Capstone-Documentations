'''
MINI PROJECT 17
You sell different chai sizes.
Instead of writing formulas everywhere, create a function.

Task:
- Write calculate_bill(cups, price_per_cup)
- Return total bill.
- Use this function for multiple orders.
'''

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2: ", calculate_bill(2, 50))