import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health🕰️")

async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 Order fetched.")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())

'''
asyncio.sleep(3) per detik:
0: background thread nyala, main thread masuk ke fetch_orders dan tunggu 3 detik.
1: background thread selesai sleep 1 detik, print logging, lanjut tunggu lagi.
2: sama kayak detik 1.
3. print logging ke-3, waktu tunggu main thread habis lalu print order fetched.
'''