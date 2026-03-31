def custom_insert(input_list, index, value):
    # Зшиваємо список: беремо частину ДО індексу + нове значення (у вигляді списку) + частину ПІСЛЯ індексу
    return input_list[:index] + [value] + input_list[index:]

if __name__ == "__main__":
    # Приклад використання програми
    original_list = [10, 20, 30, 40, 50]
    insert_index = 2
    insert_value = 99

    print(f"Початковий список: {original_list}")
    
    new_list = custom_insert(original_list, insert_index, insert_value)
    print(f"Список після вставки {insert_value} на позицію з індексом {insert_index}: {new_list}")