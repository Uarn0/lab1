def main():
    # Зчитуємо максимальне число n
    n = int(input())
    
    # Створюємо початкову множину всіх можливих чисел від 1 до n
    possible_numbers = set(range(1, n + 1))
    
    while True:
        # Зчитуємо наступний рядок
        line = input().strip()
        
        # Якщо введено слово "Все", перериваємо цикл
        if line == "Все":
            break
            
        # Перетворюємо рядок з числами на множину цілих чисел
        question_set = set(map(int, line.split()))
        
        # Визначаємо множини для відповідей "Так" і "Ні"
        yes_set = possible_numbers.intersection(question_set)
        no_set = possible_numbers.difference(question_set)
        
        # Хітрий Іван обирає більшу множину
        # Якщо множини рівні (рівно половина), він завжди каже "Ні"
        if len(yes_set) > len(no_set):
            print("Так")
            possible_numbers = yes_set
        else:
            print("Ні")
            possible_numbers = no_set

    # Виводимо числа, що залишилися, за зростанням через пробіл
    result = sorted(list(possible_numbers))
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()