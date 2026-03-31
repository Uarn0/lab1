# Варіант 1: Без генератора списку (через цикл)
def get_negatives_loop(input_list):
    negatives = []
    for num in input_list:
        if num < 0:
            negatives.append(num)
    return negatives

# Варіант 2: З використанням генератора списку
def get_negatives_comp(input_list):
    return [num for num in input_list if num < 0]

if __name__ == "__main__":
    # Приклад використання програми
    a = [12, -5, 0, 8, -3, -15, 20]
    print(f"Початковий список: {a}")
    
    print(f"Варіант 1 (без генератора): {get_negatives_loop(a)}")
    print(f"Варіант 2 (з генератором): {get_negatives_comp(a)}")