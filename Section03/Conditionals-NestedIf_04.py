'''
MINI PROJECT 04
- If the device_status is "active"
    - And temperature > 35 -> Warn: "High temperature"
    - Else: "Temperature normal"
- If device is off -> "Device is offline"
'''

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35: # Masuk karena mau cek temperatur kalau device aktif.
        print("High temperature alert!")
    else:
        print("Temperature is normal.") # Ini else dari temperatur kalau device aktif.
else:
    print("Device is offline.") # Ini else dari device aktif.