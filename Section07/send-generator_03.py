def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield # ini agar dia tidak looping terus.

stall = chai_customer()
next(stall) # Start the generator, tapi belum jalan sama sekali.

stall.send("Masala Chai") # 'send' itu interaksi langsung dengan generator.
stall.send("Lemon Chai")
# Kalau ini ga ada, code akan jalan sampai baris 2 aja,
# karena baris 3 akan dalam kondisi waiting untuk kita isi order.