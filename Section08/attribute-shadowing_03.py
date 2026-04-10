class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small"
print("After changing:", cutting.temperature)
print("Cup size:", cutting.cup)
print("Direct look into the class:", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature) # Dia bakal balik lihat ke Class utama (fallback di Class utama).
# print(cutting.cup) # Ini bakalan error karena udah dihapus di attribute, ga ada fallback di Class utama.