def print_1_to_10():
    for i in range(10):
        print(i+1)


print_1_to_10()


def print_1_to_n():
    user_numbers = int(input("Ingrese el número de elementos a imprimir: "))
    for i in range(user_numbers):
        print(i+1)


print_1_to_n()

def show_numbers_by_user() -> None:
    user_count_numbers: int = int(
        input("Ingrese cantidad de números a imprimir: "))
    numbers_to_print: str = ""

    for i in range(user_count_numbers):
        number: str = input(f"Ingrese el número {i+1}: ")
        numbers_to_print += number + ", " if i < user_count_numbers - 1 else number


    print("Los números ingresados por el usuario son:", numbers_to_print)


show_numbers_by_user()
