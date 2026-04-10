class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C):
    pass

cup = D()
print(cup.label)
'''
Dia lihat dari D dulu ada label ga, kalau ga ada..
dia ke parent, mulai dari yang pertama:
B ada label apa ga, kalau ada, dia bakal ambil labelnya dan berhenti. Ga bakal ke C.
'''
print(D.__mro__) # Ini untuk kasih tau urutannya.