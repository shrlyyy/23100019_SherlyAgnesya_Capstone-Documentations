import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3) # Non-blocking operation, jadi nanti yang ready akan muncul bersamaan, hasilnya "brewing ..." dan "... ready" satu kali sekaligus. Waktu tunggu 3 Chai ready cuma 3 detik, bukan 9 detik. Kalau pakai time.sleep dia munculnya "brewing..", "... ready", "brewing ...", "... ready"
    print(f"  {name} is ready.")

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )

asyncio.run(main())