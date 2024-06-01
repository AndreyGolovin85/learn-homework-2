"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def read_file(file) -> str:
    with open(file, "r", encoding="utf8") as file:
        lines = " ".join([line.rstrip() for line in file])
    return lines


def safe_file(file, text):
    with open(file, "w", encoding="utf8") as file:
        file.write(text)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(len(read_file("referat.txt")))
    print(len(read_file("referat.txt").split(" ")))
    print(read_file("referat.txt").replace(".", "!"))
    safe_file("referat2.txt", read_file("referat.txt"))


if __name__ == "__main__":
    main()
