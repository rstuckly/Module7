from sortedcontainers import SortedDict

"""I did the optional section on deleting a user by name or username, but I feel that
there is probably a much more efficient way of doing it.  I put the values into a list
and then got the index of the value the user entered for the username.  I then used
that position to delete the same position in the dictionary for the key in that position. I
realize that dictionarys aren't an ordered structure and positions can change, but at
least in this instance it seems to work.  """

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("\nYou must enter an integer between 1 and 5.\n")
    
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        y =(usernames.values())
        z = input("Please enter either a name or username:")
        try:
            if z in usernames.keys():
                del usernames[z]
            elif (y.index(z)):
                pos = y.index(z)
                del usernames[(usernames.keys()[pos])]
        except ValueError:
            print("\nThe name or username entered is not in the dictionary.\n")



    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("The username for {} is: {}".format(name,usernames[name]))
        else:
            print("Name not found")
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
