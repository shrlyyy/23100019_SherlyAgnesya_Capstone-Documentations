favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais}
print(unique_chai)


recipes = {
    "Masala Chai": ["Ginger", "Cardamom", "Clove"],
    "Elaichi Chai": ["Cardamom", "Milk"],
    "Spicy Chai": ["Ginger", "Black Pepper", "Clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)