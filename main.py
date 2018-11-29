from UserInterface import *
from ex import *


print("Program is running.\n"
      "Enter the name for data base file.\n"
      "Notice, that you shall type a pure name and\n"
      "if file exists it shall be located in current directory.")

inputLine = input('>> ')

while 1:
    try:
        contact_list = open_json(inputLine)
        break
    except PairExistException as e:
        print("*** Pair " + str(e) + " mentioned in file twice! ***\n"
                                     "*** Pair shall be unique. Please, enter new filename ***")
        inputLine = input('>> ')
    except IOError:
        print("*** Incorrect input! Try again ***")
        inputLine = input('>> ')

filename = inputLine

# TODO:
#  - Create a better designed user interface
#  - Implement add, find, remove, edit, print(filtered) options
#  - Implement format checking for string
#  - Implement converting for 'number' and 'birthdate'

print("\nNow, you are able to chose one of the following features:\n"
      " - add <Name> <Surname> <Number> (<Birthdate> - optional)\n"
      " - find <Name> <Surname> <Number> <Birthdate> (Each parameter is optional, required one at least)\n"
      " - remove <Name> <Surname> <Number> <Birthdate>\n"
      " - edit <Name> <Surname> <Number> <Birthdate>\n"
      " - print <Name> <Surname> <Number> <Birthdate>\n"
      " - print all\n"
      " - help  or  <command> help"
      "In order to terminate program enter:"
      " - shut down")

inputLine = input('>> ')

while 1:
    input_list = list(inputLine.split(" "))

    # ADD
    # TODO now, <add> function take a Name and Surname without Space char
    if input_list[0] == 'add':
        try:
            add(input_list, contact_list)
        except NameException:
            print("*** Unacceptable Name entered! Call <help> to check the convention ***")
        except SurnameException:
            print("*** Unacceptable Surname entered! Call <help> to check the convention ***")
        except NumberException:
            print("*** Unacceptable Number entered! Call <help> to check the convention ***")
        except DateException:
            print("*** Unacceptable Date entered! Call <help> to check the convention ***")
        except WrongParamNumber:
            print("*** Expected 3 or 4 parameters. Found " + str(len(input_list) - 1) + " ***")
    # FIND
    elif input_list[0] == 'find':
        try:
            find(input_list, contact_list)
        except NoneParamFound:
            print("*** None parameter has been found! Try again ***")
        except NameException:
            print("*** Incorrect Name parameter ***")
        except SurnameException:
            print("*** Incorrect Surname parameter ***")
        except NumberException:
            print("*** Incorrect Number parameter ***")
        except DateException:
            print("*** Incorrect Date parameter ***")

    # TODO remove existing contact from contact_list

    # TODO:
    #  - edit existing contact
    #  - edit contact in certain field

    # TODO print certain entry

    # TODO help option


    # SHUT DOWN
    elif input_list[0] == "shut" and input_list[1] == "down":
        print("Program has been shut down.\n"
              "Contact list has been saved to " + filename + "file")
        break

    # PRINT
    elif input_list[0] == 'print':
        if input_list[1] == 'all':
            contact_list.print()

    # ERROR
    else:
        print("*** Wrong input ***")
    inputLine = input('>> ')