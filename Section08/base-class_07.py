class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        # Dua di atas ini namanya code duplication (tidak disarankan).
        self.spice_level = spice_level

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength) # Ini explicit call, parent kita isi sendiri. tapi kalau ada perubahan, ubah manual.
        self.spice_level = spice_level

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength) # Ini langsung cari parent pakai 'super', kita minta dia masukin self itu buat kita langsung.
        self.spice_level = spice_level

