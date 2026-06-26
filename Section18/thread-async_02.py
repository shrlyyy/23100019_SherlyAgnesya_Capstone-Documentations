import asyncio
import time
from concurrent.futures import ThreadPoolExecutor # Jalankan kumpulan thread.

def check_stock(item, stock):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation.
    # return f"{item} stock: 42"
    return f"{item} stock: {stock}"

async def main():
    loop = asyncio.get_running_loop()

    items = [
        {"name": "Masala Chai", "stock": 42},
        {"name": "Ginger Chai", "stock": 25},
        {"name": "Oolong Tea", "stock": 18},
    ]

    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, check_stock, item["name"], item["stock"])
            for item in items
        ]
    # Jadi ini tiap item ada di thread yang berbeda, disini ada 3 thread yang isinya cuma 1 teh. Kalau di contoh async-two itu dia 3 sekaligus dalam 1 thread.
    
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())