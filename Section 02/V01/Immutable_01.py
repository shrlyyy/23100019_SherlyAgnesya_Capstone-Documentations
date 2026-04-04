sugar_amount = 2
print(f"Initial Sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial Sugar: {sugar_amount}")

"""
Ini mungkin kelihatannya kayak kita ganti sugar amount dari 2 ke 12,
padahal ketika kita tambahkan 12, Python akan tambahkan dia ke kotak yang sama dengan 2 (beda alamat aja).
Lalu dia pointing ke alamat yang paling baru sekarang, tapi 2 ini tetap masih ada dalam kotak itu.
"""

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
# Bisa dilihat waktu dijalankan, dua ID ini ada di alamat yang beda.