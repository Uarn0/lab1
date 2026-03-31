def get_common_and_different(list1, list2):
    # Перетворюємо списки на множини, щоб прибрати дублікати
    set1 = set(list1)
    set2 = set(list2)

    # Знаходимо спільні елементи (перетин множин за допомогою оператора &)
    common_elements = list(set1 & set2)

    # Знаходимо різні елементи (симетрична різниця за допомогою оператора ^)
    # Це елементи, які є або в першій, або в другій множині, але не в обох одночасно
    different_elements = list(set1 ^ set2)

    return common_elements, different_elements

if __name__ == "__main__":
    # Приклад використання
    list_a = [1, 2, 3, 4, 5, 2, 1] # Зверніть увагу на дублікати
    list_b = [4, 5, 6, 7, 8, 4, 5] # Зверніть увагу на дублікати

    print(f"Перший список: {list_a}")
    print(f"Другий список: {list_b}")
    print("-" * 30)

    common, different = get_common_and_different(list_a, list_b)

    print(f"Список спільних елементів: {common}")
    print(f"Список різних елементів: {different}")