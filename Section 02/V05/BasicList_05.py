ingredients = ["water", "milk", "black tea"]
print(f"Ingredients are: {ingredients}")

# Ketika kita lupa tambah salah satu list, pakai append.
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

# Kalau mau hapus salah satu dari list, pakai remove.
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# Mau tambahin spice ke chai, pakai extend. Ini gabungkan isi ke satu list.
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

# Kalau mau tambahkan list ke urutan spesifik, pakai insert lalu tulis posisi yang mau diselipkan.
chai_ingredients.insert(2, "black tea")
print(f"Chai: {chai_ingredients}")

# Hapus list dari posisi tertentu.
last_added = chai_ingredients.pop()
print(f"{last_added}")
# Pop ini hapus dari yang paling terakhir.
print(f"Chai: {chai_ingredients}")

# Kalau mau tukar posisi yang akhir jadi awal.
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")