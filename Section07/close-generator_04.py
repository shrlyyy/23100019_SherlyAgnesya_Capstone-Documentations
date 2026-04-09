def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()
# 'yield from' itu untuk gabungkan beberapa generator jadi satu.

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order..."
    except:
        print("Stall closed, no more chai.")

stall = chai_stall()
print(next(stall))
stall.close() # Clean up (memory). Dia langsung GeneratorExit dan keluar dari loop.