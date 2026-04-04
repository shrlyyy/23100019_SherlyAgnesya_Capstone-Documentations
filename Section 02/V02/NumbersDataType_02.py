# Integer
black_tea_grams = 14
ginger_grams = 2

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

# / ini tampilkan desimal, // ini tampilkan pembulatan

total_candamom_pods = 10
pods_per_cup = 3
leftover_pods = total_candamom_pods % pods_per_cup
print(f"Leftover candamom pods {leftover_pods}")

# % untuk tampilkan sisa pembagian

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")
# untuk dipangkatkan

total_tea_leaves_harvested = 1_000_000_000 #boleh di-separate pakai _ untuk readibility jadi ga bingung karena nolnya banyak
print(f"Tea leaves: {total_tea_leaves_harvested}")