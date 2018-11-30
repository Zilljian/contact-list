from Contact import Contact
import json
from ex import *
import datetime


"""
Class containing all contacts and provide methods to manipulate them
"""


class ContactList:
    __contact_list = list()
    __json_file_name = ""
    __contacts_number = 0

    def __init__(self, json_name):
        self.__json_file_name = json_name
        self.__initialize_list()
        self.__contacts_number = self.__contact_list.__len__()
        if self.__contacts_number == 0:
            print("\n=== Initial contact list is empty ===\n")
        else:
            print("\n=== Successfully upload stored contact list ===\n"
                  "    Number of contacts = " + str(self.__contacts_number))
        self.__push_to_data_base()
        try:
            self.__init_name_list()
        except PairExistException as e:
            raise PairExistException(str(e))

    def __initialize_list(self):
        with open(self.__json_file_name, "r") as json_handler:
            try:
                self.__contact_list = json.load(json_handler, object_hook=Contact.decode)
            except json.decoder.JSONDecodeError:
                self.__contact_list = list()

    def __push_to_data_base(self):
        with open(self.__json_file_name, "w") as json_handler:
            json.dump(self.__contact_list, json_handler, default=Contact.encode, indent=4)

    def add_contact(self, name, surname, number, date=None):
        self.__contact_list.append(Contact(name, surname, number, date))
        self.__contacts_number = self.__contact_list.__len__()
        self.__name_list.append((name, surname))
        self.__push_to_data_base()

    def get_matched(self, name=None, surname=None, number=None, date=None):
        if name and surname and number and date:
            raise NoneParamFound
        else:
            temp_list = list()
            if name is not None:
                for item in self.__contact_list:
                    if item.get_name() == name:
                        temp_list.append(item)

            if surname is not None:
                contraction = list()
                temp = temp_list if len(temp_list) != 0 else self.__contact_list

                for item in temp:
                    if item.get_surname() == surname:
                        contraction.append(item)
                temp_list = contraction

            if number is not None:
                contraction = list()
                temp = temp_list if len(temp_list) != 0 else self.__contact_list

                for item in temp:
                    temp2 = item.get_number_list()
                    for value in temp2:
                        if value == number:
                            contraction.append(item)
                            break
                temp_list = contraction

            if date is not None:
                date_sp = date.split('/')
                temp_date = datetime.date(int(date_sp[2]), int(date_sp[1]), int(date_sp[0]))
                contraction = list()
                temp = temp_list if len(temp_list) != 0 else self.__contact_list

                for item in temp:
                    if item.get_birth_date() == temp_date:
                        contraction.append(item)
                temp_list = contraction

            return temp_list

    def remove_contact(self, name, surname):
        for item in self.__contact_list:
            if item.get_name() == name and item.get_surname() == surname:
                self.__contact_list.remove(item)
        self.__contacts_number -= 1

        for item in self.__name_list:
            if item[0] == name and item[1] == surname:
                self.__name_list.remove(item)
        self.__push_to_data_base()

    def print_all(self):
        for item in self.__contact_list:
            item.print_contact()

    def __init_name_list(self):
        self.__name_list = list()

        for item in self.__contact_list:
            if (item.get_name(), item.get_surname()) not in self.__name_list:
                self.__name_list.append((item.get_name(), item.get_surname()))
            else:
                raise PairExistException(str(item.get_name()) + str(item.get_surname()))

    def get_name_list(self):
        return self.__name_list
