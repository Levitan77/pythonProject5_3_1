# Памятка:
# int() - целое число
# str() - строка
# list() - список
# tuple() - кортеж
# dict() -  словарь
# set() - множество

# Создаем функцию подсчета суммы всех чисел и длин всех строк
def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, int):  # Проверяем содержаться ли в data_structure типы int
        sum += data_structure  # если содержаться, то суммируем все числа int
    if isinstance(data_structure, str):  # Проверяем содержаться ли в data_structure типы str
        sum += len(data_structure)  # если содержаться, то суммируем количество длин всех строк str
    if isinstance(data_structure, list):  # Проверяем содержаться ли в data_structure типы list
        for i in data_structure:
            sum += calculate_structure_sum(i)  # если содержаться, то суммируем количество длин всех строк list
    if isinstance(data_structure, tuple):  # Проверяем содержаться ли в data_structure типы tuple
        for i in data_structure:
            sum += calculate_structure_sum(i)  # если содержаться, то суммируем количество длин всех строк tuple
    if isinstance(data_structure, set):  # Проверяем, содержиться ли в data_structure типы set
        for i in data_structure:
            sum += calculate_structure_sum(i)  # если содержаться, то суммируем количество длин всех строк set
    if isinstance(data_structure, dict):  # Проверяем содержаться ли в data_structure типы dict
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)  # если содержаться, то суммируем количество длин всех строк ключей
            sum += calculate_structure_sum(value)  # если содержаться, то суммируем количество длин всех строк значений
    # Возвращаем сумму
    return sum


# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Вывод результата
result = calculate_structure_sum(data_structure)
print(result)