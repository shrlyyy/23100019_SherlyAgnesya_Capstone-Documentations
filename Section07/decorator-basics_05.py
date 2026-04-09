from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs.")
        func()
        print("After function runs.")
    return wrapper

@my_decorator # Ini biar masukin func di bawah ke func my_decorator.
def greet():
    print("Hello from decorators class!")

greet()
print(greet.__name__)
# Agar output-nya bukan "wrapper", dipakai '@wraps(func)'
# as label untuk tempelkan dia balik ke identitas asli.
# Wrapper pakai identitas greet.
