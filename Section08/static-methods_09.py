class ChaiUtils:
    @staticmethod # Ngekos di Class ini untuk jalanin tugas spesifik aja.
    def clean_ingredients(text): # Terima dalam bentuk teks.
        return [item.strip() for item in text.split(",")]
        # 'split' itu ubah string jadi list.
        # kalau input kan pasti beda-beda, makanya pakai 'strip' untuk hapus spasi di awal atau akhir kata.
raw = "water , milk , ginger , honey"

cleaned = ChaiUtils.clean_ingredients(raw) # Langsung ambil dari ChaiUtils untuk dipakai.
print(cleaned)