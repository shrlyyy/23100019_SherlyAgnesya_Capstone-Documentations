chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please!")
# "f" di depan itu artinya formatted string yang bisa kita masukkin variabel (pakai tanda {}).

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}") # Ini artinya ambil dari awal sampai sebelum urutan ke-8.
print(f"First word: {chai_description[0:8:2]}") # Ini artinya ambil dari 0 sampai 8, tapi lompat setiap 2 karakter.
print(f"Last word: {chai_description[12:]}") # Ambil dari urutan ke-12 sampai habis.
print(f"Last word: {chai_description[: :-1]}") # Ini bisa dipakai untuk membalik katanya karena dia baca teks dari belakang ke depan.

# Special character
label_text = "Chai Spěcial"
ecoded_label = label_text.encode("utf-8")
# Encode ini dilakukan untuk ubah teks menjadi bytes karena sistem tidak mengerti special character tadi.
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}") # Ini hasilnya akan jadi bytes.

# Kenapa utf-8? Karena ini standar internasional yang bisa baca hampir semua karakter termasuk emoji.

decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
# Ini di-decode agar bisa dibaca lagi yang tadi di-encode menjadi teks yang bisa dibaca; makanya dia ambil dari si encode.

