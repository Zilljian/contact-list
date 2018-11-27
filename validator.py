import re
import datetime


def name_is_valid(name):
    if isinstance(name, str):
        return re.fullmatch("\b[A-Z]{1}[A-Za-z0-9 ]+\b", name)
    raise TypeError


def surname_is_valid(surname):
    if isinstance(surname, str):
        return re.fullmatch("\b[A-Z]{1}[A-Za-z0-9 ]+\b", surname)
    raise TypeError


def date_is_valid(date):
    if isinstance(date, str):
        if not re.fullmatch("\d{2}[/ ,.:;]+\d{2}[/ ,.:;]+\d{2}", date):
            return False

        day, month, year = date.split("[/ ,.:;]+")

        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            return False
        return True
    raise TypeError


def number_is_valid(number):
    if isinstance(number, int):
        number = str(number)
        number = re.sub("[- ]*", ' ', number)
        return re.fullmatch("(?:\+7|8)\d{10}", number)
    raise TypeError


def tag_is_valid(tag):
    if isinstance(tag, str):
        return re.fullmatch("\b[A-Z]{1}[A-Za-z0-9 ]+\b", tag)
    raise TypeError
