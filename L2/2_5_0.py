def main():
    # Початковий словник з даними (можна залишити порожнім: groups_db = {})
    groups_db = {
        "КН-21": {"count": 25, "head": "Іванов І.І."},
        "ПЗ-22": {"count": 18, "head": "Петренко П.П."},
        "КІ-23": {"count": 32, "head": "Сидоренко С.С."}
    }

    while True:
        print("\n" + "="*40)
        print("МЕНЮ ПРОГРАМИ:")
        print("1. Кількість студентів у зазначеній групі")
        print("2. ПІБ старости у зазначеній групі")
        print("3. Кортеж груп (кількість студентів <= заданої)")
        print("4. Кортеж груп (кількість студентів >= заданої)")
        print("5. Зміна кількості студентів у групі")
        print("6. Зміна ПІБ старости у групі")
        print("7. Додавання нової групи")
        print("8. Видалення групи")
        print("9. Множина ПІБ старост зазначених груп")
        print("10. Вихід з програми")
        print("="*40)

        choice = input("Оберіть пункт меню (1-10): ")

        if choice == '1':
            group = input("Введіть назву групи: ")
            if group in groups_db:
                print(f"Кількість студентів у групі {group}: {groups_db[group]['count']}")
            else:
                print("Групу не знайдено.")

        elif choice == '2':
            group = input("Введіть назву групи: ")
            if group in groups_db:
                print(f"ПІБ старости групи {group}: {groups_db[group]['head']}")
            else:
                print("Групу не знайдено.")

        elif choice == '3':
            try:
                limit = int(input("Введіть максимальну кількість студентів: "))
                # Створюємо кортеж
                result_tuple = tuple(g for g, data in groups_db.items() if data['count'] <= limit)
                print(f"Групи, де студентів не більше {limit}: {result_tuple}")
            except ValueError:
                print("Помилка: потрібно ввести число.")

        elif choice == '4':
            try:
                limit = int(input("Введіть мінімальну кількість студентів: "))
                # Створюємо кортеж
                result_tuple = tuple(g for g, data in groups_db.items() if data['count'] >= limit)
                print(f"Групи, де студентів не менше {limit}: {result_tuple}")
            except ValueError:
                print("Помилка: потрібно ввести число.")

        elif choice == '5':
            group = input("Введіть назву групи: ")
            if group in groups_db:
                try:
                    new_count = int(input("Введіть нову кількість студентів: "))
                    groups_db[group]['count'] = new_count
                    print("Дані успішно оновлено!")
                except ValueError:
                    print("Помилка: потрібно ввести число.")
            else:
                print("Групу не знайдено.")

        elif choice == '6':
            group = input("Введіть назву групи: ")
            if group in groups_db:
                new_head = input("Введіть нове ПІБ старости: ")
                groups_db[group]['head'] = new_head
                print("Дані успішно оновлено!")
            else:
                print("Групу не знайдено.")

        elif choice == '7':
            group = input("Введіть назву нової групи: ")
            if group in groups_db:
                print("Така група вже існує!")
            else:
                try:
                    count = int(input("Введіть кількість студентів: "))
                    head = input("Введіть ПІБ старости: ")
                    groups_db[group] = {"count": count, "head": head}
                    print("Групу успішно додано!")
                except ValueError:
                    print("Помилка: кількість студентів має бути числом.")

        elif choice == '8':
            group = input("Введіть назву групи для видалення: ")
            if group in groups_db:
                del groups_db[group]
                print("Групу успішно видалено!")
            else:
                print("Групу не знайдено.")

        elif choice == '9':
            input_groups = input("Введіть назви груп через кому (наприклад: КН-21, ПЗ-22): ")
            # Розділяємо рядок за комами та видаляємо зайві пробіли
            group_list = [g.strip() for g in input_groups.split(',')]
            
            # Створюємо множину (set)
            heads_set = set()
            for g in group_list:
                if g in groups_db:
                    heads_set.add(groups_db[g]['head'])
                else:
                    print(f"Попередження: групу '{g}' не знайдено.")
            
            print(f"Множина ПІБ старост: {heads_set}")

        elif choice == '10':
            print("Вихід з програми. На все добре!")
            break

        else:
            print("Невірний вибір. Будь ласка, введіть число від 1 до 10.")

if __name__ == "__main__":
    main()