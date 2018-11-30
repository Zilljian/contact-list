from ContactList import ContactList
from validator import *


""" 
Functions provide committing manipulation with contact list
"""


"""
Initially open a data_base.json, or create it, if it's necessary
"""


def open_json(input_line):
    try:
        file = open(input_line, "a+")
        file.close()
        contact_list = ContactList(input_line)
        return contact_list
    except IOError:
        raise IOError


"""
Provide interface for adding new contact to the list.
Firstly, check the inputs according to conventions, then add new contact
"""


def add(contact_list):
    if isinstance(contact_list, ContactList):
        print("\n=== If you have changed your mind, just write key '-b' to come back to command selection ===\n")

        name = input('Enter new contact Name >> ')

        while not name_is_valid(name) and name != '-b':
            print("*** Unacceptable Name entered! Call <help> to check the convention ***")
            name = input('Enter new contact Name >> ')
        if name == '-b':
            return

        surname = input('Enter new contact Surname >> ')

        while not surname_is_valid(surname) and surname != '-b':
            print("*** Unacceptable Surname entered! Call <help> to check the convention ***")
            surname = input('Enter new contact Name >> ')
        if surname == '-b':
            return

        while (name, surname) in contact_list.get_name_list():
            print("*** Such pair Name-Surname already exist ***")
            add(contact_list)
            return

        number = input('Enter new contact Number >> ')
        number = re.sub("[- ]+", '', number)
        number = re.sub("\+7", '8', number)

        while not number_is_valid(number) and number != '-b':
            print("*** Unacceptable Number entered! Call <help> to check the convention ***")
            number = input('Enter new contact Number >> ')
        if number == '-b':
            return

        date = input('Enter new contact Birth date (optional, format: dd/mm/yyyy) >> ')

        while not date_is_valid(date) and date != '' and date != '-b':
            print("*** Unacceptable Date entered! Call <help> to check the convention ***")
            date = input('Enter new contact Birth date (optional) >> ')
        if date == '-b':
            return
        if date == '':
            date = None

        contact_list.add_contact(name, surname, number, date)
        print("\n=== New contact has been successfully added ===\n")
    else:
        raise TypeError


"""
Provide interface for finding a contact in the list.
Firstly, check the inputs according to conventions
"""


def find(contact_list):
    if isinstance(contact_list, ContactList):
        print("\n=== If you have changed your mind, just write key '-b' to come back to command selection ===\n")
        param = [None, None, None, None]

        name = input("Enter contact's Name >> ")
        if name == '-b':
            return

        while name != '' and not name_is_valid(name):
            print("*** Unacceptable Name entered! Call <help> to check the convention ***")
            name = input("Enter contact's Name >> ")
        if name != '':
            param[0] = name

        surname = input("Enter contact' Surname >> ")
        if surname == '-b':
            return

        while surname != '' and not surname_is_valid(surname):
            print("*** Unacceptable Surname entered! Call <help> to check the convention ***")
            surname = input("Enter contact's Surname >> ")
        if surname != '':
            param[1] = surname

        number = input("Enter contact's Number >> ")
        if number == '-b':
            return
        number = re.sub("[- ]+", '', number)
        number = re.sub("\+7", '8', number)

        while number != '' and not number_is_valid(number):
            print("*** Unacceptable Number entered! Call <help> to check the convention ***")
            number = input("Enter contact's Number >> ")
        if number != '':
            param[2] = number

        date = input("Enter contact's Birth date >> ")
        if date == '-b':
            return

        while date != '' and not date_is_valid(date):
            print("*** Unacceptable Date entered! Call <help> to check the convention ***")
            date = input("Enter contact's Birth date >> ")
        if date != '':
            param[3] = date

        n = 0

        for item in param:
            if item:
                break
            else:
                n += 1
        if n == 4:
            print('*** None parameter has been entered ***')
            return

        temp = contact_list.get_matched(param[0], param[1], param[2], param[3])
        if temp.__len__():
            print("\n=== Matches found: " + str(len(temp)) + " ===")
            count = 1
            for item in temp:
                print(count, end=' ')
                count += 1
                item.print_contact()
        else:
            print("=== No matches ===")

        return temp
    else:
        raise TypeError


"""
Provide interface for editing a contact in the list if such exists.
Firstly, check the inputs according to conventions
"""


def edit(contact_list):
    temp = find(contact_list)
    print("\n=== If you have changed your mind, just write key '-b' to come back to command selection ===\n")

    if temp.__len__() > 0:
        if temp.__len__() == 1:
            input_line = 0
        else:
            input_line = int(input("Enter the serial number of required contact >> ")) - 1
        while 1:
            if 0 <= int(input_line) < temp.__len__():
                ct = temp[int(input_line)]

                name = input('Enter new contact Name >> ')

                while not name_is_valid(name) and name != '' and name != '-b':
                    print("*** Unacceptable Name entered! Call <help> to check the convention ***")
                    name = input('Enter new contact Name >> ')
                if name == '-b':
                    return

                surname = input('Enter new contact Surname >> ')

                while not surname_is_valid(surname) and surname != '' and surname != '-b':
                    print("*** Unacceptable Surname entered! Call <help> to check the convention ***")
                    surname = input('Enter new contact Name >> ')
                if surname == '-b':
                    return

                while (name, surname) in contact_list.get_name_list():
                    print("*** Such pair Name-Surname already exist ***")
                    edit(contact_list)
                    return
                if name == '':
                    if surname != '':
                        ct.set_surname(surname)
                        contact_list._ContactList__push_to_data_base()
                        print("\n=== Surname has been successfully edited ===\n")
                else:
                    if surname != '':
                        ct.set_surname(surname)
                        ct.set_name(name)
                        contact_list._ContactList__push_to_data_base()
                        print("\n=== Name and Surname have been successfully edited ===\n")
                    else:
                        ct.set_name(name)
                        contact_list._ContactList__push_to_data_base()
                        print("\n=== Name has been successfully edited ===\n")

                input_tag = input("Enter Tag of contact Number "
                                  "(If there is only one number in contact enter 'Main') >> ")

                while not tag_is_valid(input_tag) and input_tag != '' and input_tag != '-b':
                    print("*** Unacceptable Tag entered! Call <help> to check the convention ***")
                    input_tag = input('Enter new contact Tag >> ')
                if input_tag == '-b':
                    return
                if input_tag != '':
                    tag = input_tag

                    number = input(
                        'Enter new number for contact >> ')

                    number = re.sub("[- ]+", '', number)
                    number = re.sub("\+7", '8', number)

                    while not number_is_valid(number) and number != '' and number != '-b':
                        print("*** Unacceptable Number entered! Call <help> to check the convention ***")
                        number = input('Enter new contact Number >> ')
                    if number == '-b':
                        return
                    if number != '':
                        ct.set_number(number, tag)
                        contact_list._ContactList__push_to_data_base()
                        print("\n=== Number has been successfully edited ===\n")

                date = input('Enter new contact Birth date (optional, format: dd/mm/yyyy) >> ')

                while not date_is_valid(date) and date != '' and date != '-b':
                    print("*** Unacceptable Date entered! Call <help> to check the convention ***")
                    date = input('Enter new contact Birth date (optional) >> ')
                if date == '-b':
                    return
                if date != '':
                    ct.set_birth_date(date)
                    contact_list._ContactList__push_to_data_base()
                    print("\n=== Birthday has been successfully edited ===\n")

                return
            else:
                print("*** Wrong range ***")
                input_line = input("Enter the serial number of required contact >> ")
    else:
        print("\n=== No matches ===\n")


"""
Provide interface for removing a contact from the list.
Firstly, check the inputs according to conventions
"""


def remove(contact_list):
    temp = find(contact_list)

    if temp.__len__() > 1:
        input_line = int(input("Enter the serial number of required contact >> ")) - 1
        while 1:
            if 0 <= input_line < temp.__len__():
                ct = temp[input_line]
                contact_list.remove_contact(ct.get_name(), ct.get_surname())
                print("\n=== Contact has been successfully removed ===\n")
                break
            else:
                print("*** Wrong range ***")
                input_line = int(input("Enter the serial number of required contact >> ")) - 1
    elif temp.__len__() == 1:
        ct = temp[0]
        contact_list.remove_contact(ct.get_name(), ct.get_surname())
        print("\n=== Contact has been successfully removed ===\n")
    else:
        print("=== No matches ===")


"""
Help for Add function
"""


def add_help():
    print("\n"
          "--- add ---\n"
          " Command adds new contact to the contact list.\n"
          " Once it's called it invite user to enter parameters of new contact:\n"
          "- <Name> - It's required parameter of the new contact.\n"
          "Name shall follow the format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Surname> - It's required parameter of new contact.\n"
          "Surname shall follow the same format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Number> - It's required parameter of new contact.\n"
          "Number shall follow the format convention:\n"
          " *Shall start with '8' and then, shall strictly contain 10 digits"
          " *'+7' will be automatically replaced by '8'\n"
          " *Symbols '-' and whitespaces are also allowed, but will be automatically removed\n"
          "- <Birthday> - It's an optional parameter.\n"
          "Date shall follow the format convention:\n"
          " *DD/MM/YYYY format\n"
          " *The given date shall precede current date\n"
          " *The other restrictions for common format of data also matter\n"
          "\n*** Notice, that Name-Surname shall be unique for each contact in the list!\n"
          "\n*** At each point user can come back to the command selection by entering '-b'\n")


"""
Help for Find function
"""


def find_help():
    print("\n"
          "--- find ---\n"
          " Command finds contact in the contact list by the given parameters, then prints contact.\n"
          "If there is more than one contact suitable, the list of contacts prints\n"
          " Once it's called it invite user to enter parameters of a contact:\n"
          "- <Name> - It's an optional parameter.\n"
          "Name shall follow the format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Surname> - It's an optional parameter.\n"
          "Surname shall follow the same format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Number> - It's an optional parameter.\n"
          "Number shall follow the format convention:\n"
          " *Shall start with '8' and then, shall strictly contain 10 digits\n"
          " *'+7' will be automatically replaced by '8'\n"
          " *Symbols '-' and whitespaces are also allowed, but will be automatically removed\n"
          "- <Birthday> - It's an optional parameter.\n"
          "Date shall follow the format convention:\n"
          " *DD/MM/YYYY format\n"
          " *The given date shall precede current date\n"
          " *The other restrictions for common format of data also matter\n"
          "\n*** Notice, that each parameter is optional, but at least ONE parameter expected!\n"
          "\n*** At each point user can come back to the command selection by entering '-b'\n")


"""
Help for Edit function
"""


def edit_help():
    print("\n"
          "--- edit ---\n"
          " Command finds a certain contact in the contact list by the given parameters, then proposes to edit any field.\n"
          " Once it's called it invite user to enter parameters of a contact, that shall be edited\n"
          "- <Name> - It's an optional parameter.\n"
          "Name shall follow the format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Surname> - It's an optional parameter.\n"
          "Surname shall follow the same format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Tag> - It's an optional parameter.\n"
          "User have a facility to add more than one number to each contact.\n"
          "In order to do that, it's required a Tag for each new number.\n"
          "Tag shall follow the format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          "- <Number> - It's an optional parameter (There is no chance to edit number without entering a Tag).\n"
          "Number shall follow the format convention:\n"
          " *Shall start with '8' and then, shall strictly contain 10 digits\n"
          " *'+7' will be automatically replaced by '8'\n"
          " *Symbols '-' and whitespaces are also allowed, but will be automatically removed\n"
          "- <Birthday> - It's an optional parameter.\n"
          "Date shall follow the format convention:\n"
          " *DD/MM/YYYY format\n"
          " *The given date shall precede current date\n"
          " *The other restrictions for common format of data also matter\n"
          "\n*** Notice, that each parameter is optional, but in order to find the certain contact,\n"
          "at least ONE parameter expected!\n"
          "\n*** Notice, that unique pair Name-Surname for each contact is still strictly required\n"
          "\n*** At each point user can come back to the command selection by entering '-b'\n")


"""
Help for Print all function
"""


def print_all_help():
    print("\n--- print all ---\n"
          " Command prints each entry of the contact list.\n")


"""
Help for Shut down function
"""


def shut_down_help():
    print("\n--- shut down ---\n"
          " Command terminates the program.\n")


"""
Help for Remove function
"""


def remove_help():
    print("\n"
          "--- edit ---\n"
          " Command finds a certain contact in the contact list by the given parameters, then removes it.\n"
          " Once it's called it invite user to enter parameters a contact that shall be deleted:\n"
          "- <Name> - It's an optional parameter.\n"
          "Name shall follow the format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Surname> - It's an optional parameter.\n"
          "Surname shall follow the same format convention:\n"
          " *Latin symbols only allowed\n"
          " *The first symbol shall be the capital letter, if it's not so, symbol will be automatically capitalize\n"
          " *Digits and whitespaces are allowed\n"
          "- <Number> - It's an optional parameter (Any number of a contact).\n"
          "Number shall follow the format convention:\n"
          " *Shall start with '8' and then, shall strictly contain 10 digits\n"
          " *'+7' will be automatically replaced by '8'\n"
          " *Symbols '-' and whitespaces are also allowed, but will be automatically removed\n"
          "- <Birthday> - It's an optional parameter.\n"
          "Date shall follow the format convention:\n"
          " *DD/MM/YYYY format\n"
          " *The given date shall precede current date\n"
          " *The other restrictions for common format of data also matter\n"
          "\n*** Notice, that each parameter is optional, but in order to find the certain contact,\n"
          "at least ONE parameter expected!\n"
          "\n*** At each point user can come back to the command selection by entering '-b'\n")
