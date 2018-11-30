import re
import datetime


def name_is_valid(name):
    if isinstance(name, str):
        return bool(re.match("[A-Za-z0-9 ]{2,}", name))
    raise TypeError


def surname_is_valid(surname):
    if isinstance(surname, str):
        return bool(re.match("[A-Za-z0-9 ]{2,}", surname))
    raise TypeError


def date_is_valid(date_in):
    if isinstance(date_in, str):
        if not bool(re.match("\d{1,2}/\d{1,2}/\d{4}", date_in)):
            return False

        date_sp = date_in.split("/")

        try:
            datetime.date(int(date_sp[2]), int(date_sp[1]), int(date_sp[0]))
        except ValueError:
            return False
        return True
    raise TypeError


def number_is_valid(number):
    if isinstance(number, str):
        return bool(re.match("(?:\+7|8)\d{10}", number))
    raise TypeError


def tag_is_valid(tag):
    if isinstance(tag, str):
        return bool(re.match("[A-Za-z0-9 ]+", tag))
    raise TypeError


def filename_is_valid(filename):
    if isinstance(filename, str):
        return bool(re.match("[A-Za-z_.\\\d:-]+", filename))
    raise TypeError
