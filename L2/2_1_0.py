import random

def fill_random_list(n, a, b):
    # Генеруємо список з n елементів випадковими числами від a до b включно
    return [random.randint(a, b) for _ in range(n)]

if __name__ == "__main__":
    # Приклад використання програми
    count = int(input("Введіть кількість елементів (n): "))
    start = int(input("Введіть початок інтервалу (a): "))
    end = int(input("Введіть кінець інтервалу (b): "))

    result_list = fill_random_list(count, start, end)
    print(f"Згенерований список: {result_list}")