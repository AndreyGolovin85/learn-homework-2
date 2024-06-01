"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

people = [
    {"name": "Джон", "age": 30, "job": "инженер", "gender": "мужской"},
    {"name": "Мария", "age": 25, "job": "врач", "gender": "женский"},
    {"name": "Петр", "age": 40, "job": "учитель", "gender": "мужской"},
    {"name": "Анна", "age": 35, "job": "менеджер", "gender": "женский"},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open("people.csv", "w", newline="", encoding="utf8") as csvfile:
        fieldnames = ["name", "age", "job", "gender"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in people:
            writer.writerow(person)


if __name__ == "__main__":
    main()
