
import pathlib

# Задать путь к папке
path = pathlib.Path("/Users/ekaterinaloktionova/Desktop/ПРОГРАММИРОВАНИЕ/Нетология/Задания с нетологии/home_work_3")

def read_lines(path):
    # Проход по всем файлам в директории и её подпапках
    for file in path.glob("**/*"):
        if file.is_file():  # Проверка, является ли объект файлом
            with open(file, "r", encoding="utf-8") as f:
                file_name = file.name  # Имя файла
                lines = f.readlines()  # Чтение всех строк файла
            print(f"Файл: {file_name}")
            for line in lines:
                print(line.strip())

# Вызов функции
read_lines(path)