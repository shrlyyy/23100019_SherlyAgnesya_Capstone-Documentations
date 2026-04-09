def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)
'''
Kalau pakai for loop untuk panggil yield, dia ga error kayak yang di bawah kalau yield-nya habis,
karena for loop akan otomatis berhenti waktu dia ketemu StopIteration.
'''

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai) # Print generator objects.
print(next(chai)) # Kalau kita mau lihat value-nya, tambahkan 'next'.
print(next(chai))
print(next(chai))
# print(next(chai)) # error.

# Sesuai dengan yield-nya ada berapa, jadi kita cuma bisa print sebanyak yield itu (satu per satu)
# Kalau print lebih dari itu, bakalan error.