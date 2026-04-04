spice_mix = set()

print(f"Initial Spice Mix ID: {id(spice_mix)}")
print(f"Initial Spice Mix ID: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"After Spice Mix ID: {id(spice_mix)}")
print(f"Initial Spice Mix ID: {spice_mix}")

# Meski ditambahkan isinya, ID-nya tetap sama. Dia tidak ganti pointing ke yang paling baru tapi ini equal.