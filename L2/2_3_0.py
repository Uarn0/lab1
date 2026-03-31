# Варіант 1: Без генератора списку
def remove_target_loop(input_list, target):
    result = []
    for item in input_list:
        if item != target:
            result.append(item)
    return result

# Варіант 2: З використанням генератора списку
def remove_target_comp(input_list, target):
    return [item for item in input_list if item != target]

if __name__ == "__main__":
    # Приклад використання програми
    my_list = [4, 7, 2, 7, 9, 1, 7, 3]
    n = 7
    
    print(f"Початковий список: {my_list}")
    print(f"Елемент для видалення: {n}")
    
    print(f"Варіант 1 (без генератора): {remove_target_loop(my_list, n)}")
    print(f"Варіант 2 (з генератором): {remove_target_comp(my_list, n)}")