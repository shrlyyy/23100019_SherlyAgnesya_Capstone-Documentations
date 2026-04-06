def pure_chai(cups):
    return cups * 10
# Pure function = doesn't alter any ingredient globally.

total_chai = 0



# Not recommended.
def impure_chai(cups):
    global total_chai
    total_chai += cups
# Impure function.



def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured."
    return pour_chai(n-1)
# Recursive function = they will call themself till the condition match.

print(pour_chai(3))



chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
# Mau bikin fungsi instan untuk cari strong_chai, parameternya punya logika untuk cari chai != kadak, cek di list chai_types.
# "list" di depan itu agar kita bisa lihat output dalam bentuk list.
print(strong_chai)
# Lambda = anonymous function, instant version of def