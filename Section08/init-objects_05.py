class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_ # Ini karena type itu sebenarnya operator, tapi kita mau pakai type jadi nama.
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai."
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())

'''
init itu agar semua object terisi waktu kita bikin attribute.
Lalu bisa juga di-initiate dalam satu baris langsung,
ga perlu "order.type" sama "order.size". Tapi tetap bisa kita set manual waktu bikin def,
kalau mau ganti yaudah waktu isi attribute langsung isi yang baru.
'''