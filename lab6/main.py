
from decorators import unique

def get_numbers():
    return [1, 2, 3, 2, 4, 1, 5, 3]

@unique
def show_numbers():
    return get_numbers()

print("Початковий список:", get_numbers())
print("Список без повторів:", show_numbers())
