def process_order(item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu..")
    except TypeError:
        print("Quantity must be in number.")

process_order("Ginger", 2)
process_order("Masala", "two")
'''
Ini akan jadi twotwotwotwo karena kita ga bikin quantity harus integer.
Makanya dia anggap Masala yang harganya 20 dikali dengan "two", ini yang bikin hasilnya jadi repetition "two" 20 kali.
'''

# PERBAIKAN CODE
def process_order_fixed(item, quantity):
    try:
        # Bikin quantity harus pakai integer.
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number.")
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu..")
    except TypeError as e:
        print("Error: ", e)
        
process_order_fixed("Ginger", 2)
process_order_fixed("Masala", "two")
        
