chai_type = "Plain"

def front_desk():

    def kitchen():
        global chai_type # Yang diakses itu yang ada di luar function.
        chai_type = "Irnai"

    kitchen()

front_desk()
print("Final global chai:", chai_type)