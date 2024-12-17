from fileinput import filename


def load_cook_book(filename):
    cook_book = {}  # Словарь для хранения всех рецептов
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            dish_name = f.readline().strip()  # Читаем название блюда
            if not dish_name:  # Если название пустое, прекращаем чтение
                break
            num_ingredients_line = f.readline().strip()  # Читаем количество ингредиентов
            if not num_ingredients_line:  # Если количество ингредиентов не указано, пропускаем
                continue
            try:
                num_ingredients = int(num_ingredients_line)  # Преобразуем строку в число
            except ValueError:  # Если ошибка при преобразовании, сообщаем и пропускаем
                print(f"Ошибка чтения количества ингредиентов для блюда '{dish_name}'")
                for _ in range(num_ingredients):
                    f.readline()  # Пропускаем строки с ингредиентами
                f.readline()  # Пропускаем пустую строку между блюдами
                continue

            ingredients = []  # Список для ингредиентов текущего блюда
            for i in range(num_ingredients):
                ingredients_data = f.readline().strip()  # Читаем строку с данными ингредиента
                name, quantity, measure = ingredients_data.split(" | ")  # Разделяем данные на имя, количество, единицу измерения
                ingredients.append({
                    "ingredient_name": name,  # Название ингредиента
                    "quantity": int(quantity),  # Количество ингредиента
                    "measure": measure  # Единица измерения
                })
            cook_book[dish_name] = ingredients  # Добавляем блюдо и его ингредиенты в словарь
            f.readline()  # Пропускаем пустую строку между блюдами
    return cook_book  # Возвращаем словарь с рецептами

def print_dishes_as_is(cook_book, dishes, person_count):
    # Количество персон теперь не влияет на итоговый результат
    for dish in dishes:  # Перебираем все блюда из списка
        dish = dish.strip()  # Убираем лишние пробелы
        if dish not in cook_book:  # Если блюда нет в книге рецептов
            print(f"Блюдо '{dish}' отсутствует в книге рецептов")
            continue

        dish_dict = {}  # Словарь для ингредиентов текущего блюда
        for ingredient in cook_book[dish]:  # Перебираем все ингредиенты блюда
            # Просто берем оригинальное количество и меру, не умножая
            dish_dict[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],  # Единица измерения ингредиента
                'quantity': ingredient['quantity']  # Количество ингредиента
            }

        print(dish_dict)  # Выводим ингредиенты текущего блюда



if name == "__main__":
    cook_book = load_cook_book("recipes.txt")  # Загружаем рецепты из файла

    dishes_input = input("Введите названия блюд через запятую: ")  # Запрашиваем у пользователя блюда
    dishes = [dish.strip() for dish in dishes_input.split(',')]  # Преобразуем в список, удаляя пробелы
    person_count = int(input("Введите количество персон: "))  # Запрашиваем количество персон

    # Выводим ингредиенты блюд без умножения
    print_dishes_as_is(cook_book, dishes, person_count)