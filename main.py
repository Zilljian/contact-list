from UserInterface import *

'''
Initialization file
'''

contact_list = open_json("data_base.json")

print("\nPlease, chose one of the following features:\n"
      " - add \n"
      " - find \n"
      " - edit \n"
      " - print all\n"
      " - remove \n"
      " - help <Command>\n"
      "In order to terminate program enter:\n"
      " - shut down\n")

input_line = input('>> ')

while 1:
    # ADD
    if input_line == 'add':
            add(contact_list)
    # FIND
    elif input_line == 'find':
        find(contact_list)
    # REMOVE
    elif input_line == 'remove':
        remove(contact_list)
    # EDIT
    elif input_line == 'edit':
        edit(contact_list)
    # PRINT
    elif input_line == 'print all':
        contact_list.print_all()
    # SHUT DOWN
    elif input_line == 'shut down':
        print("\n=== Program has been shut down ===\n"
              "Contact list has been saved to  data_base.json file")
        break
    elif input_line.split()[0] == 'help':
        if input_line.split()[1] == 'add':
            add_help()
        elif input_line.split()[1] == 'find':
            find_help()
        elif input_line.split()[1] == 'edit':
            edit_help()
        elif input_line.split()[1] == 'print':
            print_all_help()
        elif input_line.split()[1] == 'remove':
            remove_help()
        elif input_line.split()[1] == 'shut':
            shut_down_help()
    else:
        print("*** Wrong input ***")
    input_line = input('>> ')
