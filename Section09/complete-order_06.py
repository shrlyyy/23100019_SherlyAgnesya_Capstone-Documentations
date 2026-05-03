'''
Mini Project 19
'''

class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"Masala": 20, "Ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available.")
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an integer.")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} Chai: {total} Rupees.")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting!")

bill("Mint", 2)
bill("Masala", "three")
bill("Ginger", 3)