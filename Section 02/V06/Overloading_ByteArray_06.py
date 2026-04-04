base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# Ini namanya overloading. Bedanya dengan extend itu, kalau yang ini gabungkan 2 list jadi 1 list baru.
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

# Ini juga overloading tapi ini dia melakukan repetition (isinya disalin sebanyak n) bukan bikin list dalam list.
strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

# Ini bytearray, bisa mengubah objek bytes jadi mutable sehingga isinya bisa dimodif tanpa harus membuat objek baru.
raw_spice_data = bytearray(b"CINNAMON") # b di depan itu menandakan dia objek bytes.
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD") # Cari potongan kata "CINNA" lalu ganti jadi "CARD".
print(f"Bytes: {raw_spice_data}")
# Sebenarnya ini dia return objek baru karena pakai replace, jadi alamat memorinya akan beda dengan yang awal.
