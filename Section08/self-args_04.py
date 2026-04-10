class ChaiCup:
    size = 150 # in ml

    def describe(self): # methods. 'self' itu untuk refer ke class-nya.
        return f"a {self.size}ml chai cup."
    
cup = ChaiCup()
print(cup.describe())
print(ChaiCup.describe(cup)) # Kasih konteks mana yang mau di-print.
'''
Jadi dia kayak: pakai cetakan ChaiCup, jalanin metode describe tapi lihat data
di objek cup.
'''

cup_two = ChaiCup()
cup_two.size = 100 # Hanya ganti untuk cup two.
print(ChaiCup.describe(cup_two)) # Ini juga kasih konteks yang mana.