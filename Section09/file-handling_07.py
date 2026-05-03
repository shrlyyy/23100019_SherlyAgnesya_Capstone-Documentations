# file = open("order.txt", "w") # w = write
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()

with open("tea_order.txt", "w") as file:
    file.write("Ginger tea - 4 cups")