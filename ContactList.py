from Contact import Contact
import json
import re
from validator import \
    name_is_valid, \
    surname_is_valid, \
    date_is_valid, \
    number_is_valid, \
    tag_is_valid


class ContactList:
    __contact_list = list()
    __json_file_name = ""
    __contacts_number = 0

    def __init__(self, json_name):
        self.__json_file_name = json_name
        self.__initialize_list()
        self.__contacts_number = self.__contact_list.__len__()
        if self.__contacts_number == 0:
            print("\nInitial contact list is empty.")
        else:
            print("\nSuccessfully upload stored contact list. "
                  "Number of contacts = " + str(self.__contacts_number))

    def __initialize_list(self):
        with open(self.__json_file_name, "r") as json_handler:
            try:
                self.__contact_list = json.load(json_handler, object_hook=Contact.decode)
            except json.decoder.JSONDecodeError:
                self.__contact_list = list()

    def __push_to_data_base(self, new_contact):
        with open(self.__json_file_name, "a") as json_handler:
            json.dump(new_contact, json_handler, default=Contact.encode, indent=4)

    def add_contact(self, name, surname, number, date=None):
        self.__contact_list.append(Contact(name, surname, number, date))
        self.__push_to_data_base()

    def is_contact_in_list(self, name=None, surname=None, number=None, date=None):
        if name and surname and number and date:
            raise ValueError
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
                #number = re.sub("[- ]*", '', number)
                #number = re.sub("\b+7", '', number)
                contraction = list()
                temp = temp_list if len(temp_list) != 0 else self.__contact_list

                for item in temp:
                    for num in item.get_number_list:
                        if str(num) == number:
                            contraction.append(item)
                            break
                temp_list = contraction

            if date is not None:
                contraction = list()
                temp = temp_list if len(temp_list) != 0 else self.__contact_list

                for item in temp_list:
                    if item.get_date() == date:
                        contraction.append(item)
                temp_list = contraction

            return temp_list

    def print(self):
        for item in self.__contact_list:
            print(str(item.get_name()) + " " + str(item.get_surname()), end=' ')
            if item.get_birth_date():
                print(str(item.get_birth_date()))
            else:
                print()
            for key, value in item.get_number_list().items():
                print(key + " : " + str(value))
            print()
