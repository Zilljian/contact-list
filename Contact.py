class Contact:

    def __init__(self, name, surname, number, date=None):
        self.__name = name
        self.__surname = surname
        self.__number = {'Main': number}
        self.__birth_date = date
        self.__number_list_len = 1

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_number(self, tag='Main'):
        return self.__number[tag]

    def set_number(self, number, tag='Main'):
        self.__number[tag] = number
        self.__number_list_len = self.__number.__len__()

    def get_number_list(self):
        return self.__number

    def get_number_list_len(self):
        return self.__number_list_len

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, new_date):
        self.__birth_date = new_date

    @staticmethod
    def default(object):
        if isinstance(object, Contact):
            return {
                'Name': object.get_name(),
                'Surname': object.get_surname(),
                'Number': object.get_number_list()}
        raise TypeError