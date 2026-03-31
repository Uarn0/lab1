import math

def sum_progression(i):
    return i * (i + 1) / 2

# 1. Обчислення за допомогою циклу FOR
def calc_for(n, x):
    inner_val = 0
    # Йдемо від внутрішнього кореня (i=n) до зовнішнього (i=1)
    for i in range(n, 0, -1):
        val_under_root = sum_progression(i) + x + inner_val
        if val_under_root < 0:
            return False, None
        inner_val = math.sqrt(val_under_root)
    return True, inner_val

# 2. Обчислення за допомогою циклу WHILE
def calc_while(n, x):
    inner_val = 0
    i = n
    while i >= 1:
        val_under_root = sum_progression(i) + x + inner_val
        if val_under_root < 0:
            return False, None
        inner_val = math.sqrt(val_under_root)
        i -= 1
    return True, inner_val

# 3. Обчислення за допомогою рекурсії
def calc_recursion(n, x, current_i=1):
    # Базовий випадок: дійшли до найглибшого кореня
    if current_i == n:
        val_under_root = sum_progression(current_i) + x
        if val_under_root < 0:
            return False, None
        return True, math.sqrt(val_under_root)
    
    # Рекурсивний крок: спочатку обчислюємо внутрішній корінь
    success, inner_val = calc_recursion(n, x, current_i + 1)
    
    if not success:
        return False, None
        
    val_under_root = sum_progression(current_i) + x + inner_val
    if val_under_root < 0:
        return False, None
        
    return True, math.sqrt(val_under_root)

# Основна функція для вводу даних та виведення результатів
def main():
    try:
        n = int(input("Введіть кількість коренів n (натуральне число, n >= 1): "))
        if n < 1:
            print("Помилка: n має бути натуральним числом (1, 2, 3...).")
            return
            
        x = float(input("Введіть дійсне число x: "))
    except ValueError:
        print("Помилка вводу. Перевірте правильність введених даних.")
        return

    print("-" * 40)
    
    # Виклик функції з FOR
    success_for, result_for = calc_for(n, x)
    print("Метод FOR:")
    print(f"  Успішність: {success_for}")
    if success_for:
        print(f"  Результат:  {result_for}")

    print("-" * 40)

    # Виклик функції з WHILE
    success_while, result_while = calc_while(n, x)
    print("Метод WHILE:")
    print(f"  Успішність: {success_while}")
    if success_while:
        print(f"  Результат:  {result_while}")

    print("-" * 40)

    # Виклик функції з рекурсією
    success_rec, result_rec = calc_recursion(n, x)
    print("Метод РЕКУРСІЇ:")
    print(f"  Успішність: {success_rec}")
    if success_rec:
        print(f"  Результат:  {result_rec}")
        
    print("-" * 40)

if __name__ == "__main__":
    main()