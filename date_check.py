# Создайте модуль и напишите в нём функцию, которая получает
# на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную
# защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в
# терминале с передачей даты на проверку.


from sys import argv

__all__ = ['is_valid_date']

YEARS = range(1, 10000)
MONTHS = range(1, 13)
DAYS = range(1, 32)
SHORT_MONTH = [4, 6, 9, 10]
SHORT_MONTH_LAST_DAY = 30
FEBRUARY = 2
LEAP_FEB_LAST_DAY = 29
NORMAL_FEB_LAST_DAY = 28
LONG_MONTH_LAST_DAY = 31


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if day in DAYS and month in MONTHS and year in YEARS:
        if month in SHORT_MONTH:
            return day <= SHORT_MONTH_LAST_DAY
        elif month == FEBRUARY:
            if is_leap_year(year):
                return day <= LEAP_FEB_LAST_DAY
            else:
                return day <= NORMAL_FEB_LAST_DAY
        else:
            return day <= LONG_MONTH_LAST_DAY
    else:
        return False


if __name__ == '__main__':
    date_str = input("Введите дату в формате DD.MM.YYYY: ")
    if is_valid_date(date_str):
        print("Такая дата существует.")
    else:
        print("Такая дата не существует.")