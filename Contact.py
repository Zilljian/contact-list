class Contact:
    __name = ""
    __surname = ""
    __number = None
    __birth_date = ""

    def __init__(self, name, surname, number, date=None):
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__birth_date = date

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, new_date):
        self.__birth_date = new_date
