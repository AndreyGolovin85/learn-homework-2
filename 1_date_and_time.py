"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_today = datetime.date.today()
    yesterday = date_today - datetime.timedelta(days=1)
    thirty_days_ago = date_today - datetime.timedelta(days=30)
    print(date_today, yesterday, thirty_days_ago)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = "01/01/20 12:10:03.234567"
    date_format = "%d/%m/%y %H:%M:%S.%f"
    date_object = datetime.datetime.strptime(date_string, date_format)
    return date_object


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
