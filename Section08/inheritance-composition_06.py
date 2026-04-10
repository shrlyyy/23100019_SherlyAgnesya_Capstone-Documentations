class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} Chai...")

class MasalaChai(BaseChai): #ini dia inheritance dari BaseChai.
    def add_spices(self):
        print("Adding cardamom, ginger, and cloves...")

class ChaiShop:
    chai_class = BaseChai # Dia bikin pakai standar BaseChai.

    def __init__(self):
        self.chai = self.chai_class("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} Chai in the shop...")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_class = MasalaChai
    # Warisin standar kerja ChaiShop tapi jenisnya pakai Masala.

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve() # Pinjam method.
fancy.chai.add_spices()