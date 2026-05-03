'''
Challenge 09: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:
1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS.
- Use a beep sound ('\a') at the end if the terminal supports it.
- Prevent negative or non-integer inputs.
'''

import time

while True:
    try:
        seconds = int(input("⏰ Enter the time in seconds: "))
        if seconds < 1:
            print("Please enter a number greater than 0.")
            continue # Pakai ini agar bisa balik ke input kalau syarat tidak memenuhi.
        break # Kalau benar, loop berhenti dan lanjut.
    except ValueError:
        print("Invalid input, please enter a whole number.")

print("\n🔔 Timer started...")
for remaining in range(seconds, 0, -1): # (angka input, berhenti sebelum 0, dikurang 1 setiap putaran).
    mins, secs = divmod(remaining, 60) # fungsi pembagian & sisa bagi: remaining dibagi 60, hasil bagi disimpan di mins, sisa bagi disimpan di secs.
    time_format = f"{mins:02}:{secs:02}" # ":02" artinya menampilkan 2 angka aja (kalau 1 angka, pakai 0).
    print(f"⏰ Time left: {time_format} ", end="\r") # "\r" ini carriage return artinya kursor balik ke awal baris yang sama (angka baru akan nimpa angka lama di baris sama jadi kayak countdown).
    time.sleep(1) # berhenti 1 detik sebelum lanjut loop.

print("\nTime's up! Take a break or move on to next task.")
#print("\a") # Optional; makes a beep sound.