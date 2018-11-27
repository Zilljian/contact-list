from ContactList import ContactList
import re
from validator import filename_is_valid
from Contact import Contact
import json


print("Program is running.\n"
      "Enter the name for data base file.\n"
      "Notice, that you shall type a pure name "
      "(everything followed by '.' will be removed) and\n"
      "if file exists it shall be located in current directory.")

inputLine = input('>> ')

if filename_is_valid(inputLine):
    if not re.fullmatch("\B.json\b", inputLine):
        inputLine = inputLine + '.json'
        print(inputLine)

while 1:
    try:
        file = open(inputLine, "a+")
        file.close()
        break
    except IOError:
        print("Incorrect input! Try again")
        inputLine = input('>> ')

contact_list = ContactList(inputLine)

print("\nNow, you are able to chose one of the following features:\n"
      "- add <Name> <Surname> <Number> (<Birthdate> - optional)\n"
      "- find <Name> <Surname> <Number> <Birthdate>\n"
      "- remove <Name> <Surname> <Number> <Birthdate>\n"
      "- edit <Name> <Surname> <Number> <Birthdate>\n"
      "- print <Name> <Surname> <Number> <Birthdate>\n"
      "- print all\n"
      "Also, you can get help, just type: <command> help")

while inputLine != 'shut down':
    if list(inputLine.split(" "))[0] == 'new':
        if len(list(inputLine.split(" "))) == 4:
            temp = list(inputLine.split(" "))
            contact_list.add_contact(temp[1], temp[2], temp[3])
        elif len(list(inputLine.split(" "))) == 5:
            temp = list(inputLine.split(" "))
            contact_list.add_contact(temp[1], temp[2], temp[3], temp[4])
    elif list(inputLine.split(" "))[0] == 'print':
        if list(inputLine.split(" "))[1] == 'all':
            contact_list.print()
    inputLine = input('>> ')