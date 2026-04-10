class Chai: # Create class.
    pass

print(type(Chai))

class ChaiTime:
    pass

ginger_tea = Chai() # Create object.
print(type(ginger_tea)) # Untuk kasih tau kalau class Chai itu ada di-file yang kita jalankan. Kalau ada di-file lain, dia tampilin nama file itu.

# Untuk cek benar ga dia termasuk class ini:
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)