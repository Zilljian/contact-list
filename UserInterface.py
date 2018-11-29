from ContactList import ContactList
from ex import *
from Contact import *
from validator import *


def open_json(input_line):
    try:
        if filename_is_valid(input_line):
            if not input_line.endswith('.json'):
                input_line = input_line + '.json'

            file = open(input_line, "a+")
            file.close()
        else:
            raise IOError
    except IOError:
        raise IOError

    filename = input_line

    try:
        contact_list = ContactList(filename)
        return contact_list
    except PairExistException as e:
        raise PairExistException(str(e))


def find(input_list, contact_list):
    length = len(input_list)

    if isinstance(contact_list, ContactList):
        if length < 2:
            raise NoneParamFound
        else:
            param = [None, None, None, None, None]
            for i, item in enumerate(input_list):
                param[i] = item

            if not name_is_valid(param[1]):
                if param[1] is not None:
                    raise NameException
            elif not surname_is_valid(param[2]):
                if param[2] is not None:
                    raise SurnameException
            elif not number_is_valid(param[3]):
                if param[3] is not None:
                    raise NumberException
            elif not date_is_valid(param[4]):
                if param[4] is not None:
                    raise DateException
            else:
                temp = contact_list.get_matched(param[1], param[2], param[3], param[4])
                print("\n=== Matches found: " + str(len(temp)) + " ===")

                for item in temp:
                    item.print_contact()
    else:
        raise TypeError


def add(input_list, contact_list):
    length = len(input_list)

    if isinstance(contact_list, ContactList):
        if length == 4:
            if not name_is_valid(input_list[1]):
                raise NameException()
            if not surname_is_valid(input_list[2]):
                raise SurnameException
            if not number_is_valid(input_list[3]):
                raise NumberException
            if (input_list[1], input_list[2]) in contact_list.get_name_list():
                raise PairExistException
            else:
                contact_list.add_contact(input_list[1], input_list[2], input_list[3])
        elif length == 5:
            if not name_is_valid(input_list[1]):
                raise NameException()
            if not surname_is_valid(input_list[2]):
                raise SurnameException
            if not number_is_valid(input_list[3]):
                raise NumberException
            if not date_is_valid(input_list[5]):
                raise DateException
            if (input_list[1], input_list[2]) in contact_list.get_name_list():
                raise PairExistException
            else:
                contact_list.add_contact(input_list[1], input_list[2], input_list[3], input_list[4])
                print("\n=== New contact has been successfully added ===\n")
        else:
            raise WrongParamNumber
    else:
        raise TypeError

# TODO remove existing contact from contact_list

# TODO:
#  - edit existing contact
#  - edit contact in certain field

# TODO print certain entry

# TODO help option
