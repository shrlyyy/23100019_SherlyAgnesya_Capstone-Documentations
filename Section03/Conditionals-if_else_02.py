'''
MINI PROJECT 02
A local cafe wants a program that suggests a snack.
If a customer asks for cookies or samosa, it confirms the order.
Otherwise, it says it's not available.

Task:
- Take snack input.
- If it's "cookies" or "samosa", confirm the order
- Else, show unavailability
'''

snack = input("Enter your preferred snack: ").lower() # Ini untuk user input. Lower itu untuk bikin apapun yang di-input jadi lowercase.

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}!")
else:
    print("Sorry, we only serve cookies or samosa with tea.")
