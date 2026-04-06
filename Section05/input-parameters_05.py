# chai = "Ginger Chai"

# def prepare_chai(order):
#     print(f"Preparing", order)

# prepare_chai(chai)
# print(chai)

# '''
# Bisa print Ginger Chai itu karena chai yang global tadi
# kalau dalam function itu jadi order (local).
# Kenapa ga panggil pakai global?
# Ini karena dalam local juga ga ada define chai baru, makanya dia lihat ke global.
# '''



chai = [1, 2, 3] # Ingat ini bacanya pakai list jadi dari 0 (= 1), 1 (= 2), 2 (= 3).

def edit_chai(cup):
    cup[1] = 42 # Artinya dia ubah yang ke-1 = 2

edit_chai(chai)
print(chai)



def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keyword



def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Cinnamon", "Cardamom", sweetener = "Honey", foam = "yes")

'''
Kenapa yang Cinnamon dan Cardamom masuk ke ingredients, sisanya masuk ke extras?
Ini karena tanda * (args) itu anggapannya dia khusus 'borongan' input untuk isi yang kita bikin (ga ada label khusus) ke tuple.
Sedangkan, tanda ** (kwargs) itu khusus input 'label suka-suka' yang diisi waktu inputnya, jadi dia ngisi label baru dan isinya.
'''



# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
