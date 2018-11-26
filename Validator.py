import re
import datetime


def name_validator(name):
    return re.fullmatch("\b[A-Z]{1}[A-Za-z0-9 ]+\b", name)


def surname_validator(surname):
    return re.fullmatch("\b[A-Z]{1}[A-Za-z0-9 ]+\b", surname)


def date_validator(date):
    if not re.fullmatch("\d{2}[/ ,.:;]+\d{2}[/ ,.:;]+\d{2}", date):
        return False

    day, month, year = date.split("[/ ,.:;]+")

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    return True


def number_validator(number):
    number = re.sub("[- ]*", number)
    return re.fullmatch("(?:\+7|8)\d{10}", number)
