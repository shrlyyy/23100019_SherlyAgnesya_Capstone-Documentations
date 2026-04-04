is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling #upcasting, angka True dianggap 1 jadi dipakai sama dia untuk menghitung.

print(f"Total actions: {total_actions}")

milk_present = 0 #no milk in stock
print(f"Is there a milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can I serve chai? {can_server}" )
# Yang ini bisa pakai AND, OR, sama NOT, aturannya sama kayak di MTK.
