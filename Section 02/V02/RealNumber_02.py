import sys
from fractions import Fraction
from decimal import Decimal 

ideal_temp = 95.5
current_temp = 95.4999

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
# Hasilnya bakalan banyak angka di belakang koma karena sistem itu pakai biner, desimal itu ga bisa dikonversi sempurna ke biner.
# Makanya di-import sys untuk bisa dipakai untuk akurasi presisi perhitungan tadi. Dia akan memverifikasi batas presisi sistemnya.

print(sys.float_info) # Ini untuk lihat spesifikasinya.

precise_diff = Decimal('95.5') - Decimal('95.4999')
print(f"Precise Difference: {precise_diff}");
# Pakai 'Decimal' karena kita butuhnya untuk hitung suhu (bisa juga untuk uang).
# Kalau untuk nilai pecahan murni tanpa desimal yang hilang, pakai 'Fraction'.