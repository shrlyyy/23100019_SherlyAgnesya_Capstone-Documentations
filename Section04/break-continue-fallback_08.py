'''
MINI PROJECT 13
Some chai flavors are out of stock.
You want to skip those and stop entirely if
someone requests a restricted flavor.

Task:
- Skip if flavor is "Out of Stock"
- Break is flavor is "Discontinued"
'''

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found.")
        break
    print(f"{flavour} item found.")
print(f"Out side of loop")