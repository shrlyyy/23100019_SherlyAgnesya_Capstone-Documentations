chai_menu = {"Masala": 30, "Ginger": 40}

# chai_menu["Elaichi"] # Ini akan tampilkan KeyError.

try:
    chai_menu["Elaichi"]
except KeyError: # Ini artinya kalau ketemu KeyError dia akan tampilkan:
    print("The key thay you're trying to access doesn't exists.")

print("Hello Chai-code!")
