import datetime
import re


"""
Class for carrying the entity of contact
"""


class Contact:

    def __init__(self, name, surname, number, date=None):
        self.__name = name.capitalize()
        self.__surname = surname.capitalize()
        if isinstance(number, str):
            self.__number = {'Main': number}
        else:
            self.__number = number
        if date:
            date_sp = re.split("/", date)
            if date_sp.__len__() != 1:
                self.__birth_date = datetime.date(int(date_sp[2]), int(date_sp[1]), int(date_sp[0]))
            else:
                date_sp = re.split("[-T]", date)
                self.__birth_date = datetime.date(int(date_sp[0]), int(date_sp[1]), int(date_sp[2]))
        else:
            self.__birth_date = date
        self.__number_list_len = self.__number.__len__()

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name.capitalize()

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname.capitalize()

    def get_number(self, tag='Main'):
        return self.__number[tag]

    def set_number(self, number, tag='Main'):
        self.__number[tag.capitalize()] = number
        self.__number_list_len = self.__number.__len__()

    def get_number_list(self):
        temp = list()
        for key in self.__number:
            temp.append(self.__number[key])
        return temp

    def __get_number_dict(self):
        return self.__number

    def get_number_list_len(self):
        return self.__number_list_len

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, new_date):
        date_sp = new_date.split("/")
        self.__birth_date = datetime.datetime(int(date_sp[2]), int(date_sp[1]), int(date_sp[0]))

    @staticmethod
    def encode(obj):
        if isinstance(obj, Contact):
            return {
                'Name': obj.get_name(),
                'Surname': obj.get_surname(),
                'Number': obj.__number,
                'Date': obj.get_birth_date()}
        elif isinstance(obj, datetime.date):
            return obj.isoformat()

    @staticmethod
    def decode(dct):
        if "Name" in dct:
            return Contact(dct['Name'], dct['Surname'], dct['Number'], dct['Date'])
        return dct

    def print_contact(self):
        print(self.__name + " " + self.__surname)
        if self.__birth_date:
            print("Birthday: " + str(str(self.__birth_date.day) + "/" +
                  str(self.__birth_date.month) + "/" +
                  str(self.__birth_date.year)), end=' ')
            today = datetime.date.today()
            years = today.year - self.__birth_date.year
            if today.month < self.__birth_date.month or \
                    (today.month == self.__birth_date.month and today.day < self.__birth_date.day):
                years -= 1
            print("(" + str(years) + " years)")
        else:
            print()
        for key, value in self.__number.items():
            print(key + " : " + str(value))
        print()
