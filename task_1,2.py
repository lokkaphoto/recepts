cook_book = {}

with open("recipes.txt", "r", encoding = "utf - 8") as f:
    while True:
        dish_name = f.readline().strip() # читаем каждую строку и удаляем пробелы
        if not dish_name:  # если не можем прочитать что написано в строке
            break # конец файла
        num_ingridients_line = f.readline().strip() # колличество ингридиентов
        if not num_ingridients_line:
            continue # пропустить итерацию
        try:
            num_ingridients = int(num_ingridients_line)
        except ValueError:
            print(f"Ошибка чтения колличества ингридиентов для блюда '{dish_name}'")
            continue
        ingridients = []
        for i in range(num_ingridients):
            ingridients_data = f.readline().strip() # читаем строку с данными об ингридиенте
            name, quantity, measure = ingridients_data.split(" | ")
            ingridients.append({
                "ingridients_name": name,
                "quantity" : int(quantity),
                "measure" : measure
            })
        cook_book[dish_name] = ingridients # добавляем блюдо и список его ингридиентов в словарь coock_book
        f.readline()
for dish, ingridients in cook_book.items(): # Проходим по всем блюдам и ингридиентам в списке
    print(f"{dish}:") # Выводим название блюда
    for ingridient in ingridients: # Проходим по списку ингридиентов для текущего блюда
        print(f" {ingridient}") # Выводим информацию об ингридиенте с отступом
    print()
dishes = ['Запеченный картофель', 'Омлет', 'Фахитос', 'Утка по-пекински'] #Список блюд в кнге рецептов
person_count = 2


def get_shop_list(dishes, person_count):
    shop_list = {}  # список покупок

    for dish in dishes: # Проходим по всем блюдам в списке
        if dish in cook_book: # Если блюдо есть в списке рецептов
            for ingridient in cook_book[dish]:
                name = ingridient['ingridients_name'] # Имя блюда
                quantiity = ingridient['quantity'] * person_count # Колличество ингридиентов
                measure = ingridient['measure'] # Еденицу измерения ингридиентов
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantiity}
                else:
                    shop_list[name]['quantity'] += quantiity

        else:
            print(f"Блюдо '{dish}' отсутствует в книше рецептов") # Если блюдо отсутствует в книге рецептов

        return shop_list

# Выводим функцию
shop_list = get_shop_list(dishes, person_count)

for ingridient, details in shop_list.items():
    print(f"{ingridient}: {details}")





