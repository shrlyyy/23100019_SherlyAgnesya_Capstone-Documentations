def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} Chai...")
        if flavor == "unknown": # Kalau ketemu "unknown":
            raise ValueError("We don't know that flavor.") # Dia kasih tau ada masalah pakai raise.
    except ValueError as e:
        print("Error: ", e) # Yang di-raise tadi dijadikan except buat error-nya.
    else: # Kalau semuanya lancar:
        print(f"{flavor} Chai is served.")
    finally: # Apapun yang terjadi, mau itu ada masalah atau lancar jaya, kita bisa munculin pesan pakai finally sebagai penutup.
        print("Next customer please!")

serve_chai("Masala")
serve_chai("unknown")