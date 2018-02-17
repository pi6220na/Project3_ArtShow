from artists import Artists
from items import Items
from sales import Sales
from show import Show
import g

# the following clear screen technique works on windows machines when running the .py file in a terminal or CMD prompt
# it does not work within the pyCharm run window and instead shows a  symbol
import os  # clear screen technique: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
clear = lambda: os.system('cls')


def print_main_menu():
    clear()

    valid = False
    choice = ''

    message('********** Welcome to the Art Show Database Program ***********')
    message('')
    message('1) Add show info: Artists, Items, and Shows')
    message('2) Add a Sales record for a Show')
    message('3) Modify a Record: Artists, Items, Shows, and Sales')
    message('4) Delete a Record: Artists, Items, Shows, and Sales')
    message('5) Show Info: Artists, Items, Shows, and Sales')
    message('6) Analysis on Records')
    message('"q" to quit the program')
    message('')

    while not valid:

        choice = input('Enter 1, 2, 3, 4, or 5 or q: ')
        if (choice != '1' and choice != '2' and choice != '3' and choice != '4'
                and choice != '5' and choice != 'q'):
            message('Error, please enter 1, 2, 3, 4, or 5 or q to quit: ')
        else:
            valid = True

    return choice


def add_show_info():
    clear()

    valid = False
    choice_1 = ''

    message('')
    message('  Add Show Information')
    message('1) Add Artists Record')
    message('2) Add Art Items Record')
    message('3) Add Shows Record')
    message('"q" to return to main menu')
    message('')

    while not valid:

        choice_1 = input('Enter 1, 2, 3, or q: ')
        if (choice_1 != '1' and choice_1 != '2' and choice_1 != '3' and choice_1 != 'q'):
            message('Error, please enter 1, 2, 3, or q to return: ')
        else:
            valid = True

    message('returning choice_1 = {}'.format(choice_1))
    return choice_1


def add_sales_record():
    '''This function will add a sales record to the sales_list list
       the function will rely on the database to catch any foreign key mis-match errors'''
    clear()
    message('*** Enter a Sales Record ***')
    message('')
    message('*** Here are the available Items. The item ID must be specified')
    message('    when adding a sales item.')
    for item in g.items_list:
        message(item)
    message('')
    message('*** Here are the available Shows. The show ID must be specified')
    message('    when adding a sales item.')
    for show in g.show_list:
        message(show)
    message('')

    while True:
        clear()
        saleitemid = input('Enter the item ID of the sale item (an integer from above list): ')
        salequantity = input('Enter the quantity of sales items sold: ')
        saletotal = input('Enter the total sale dollar amount: ')
        showid = input('Enter the Show ID (an integer from the above list): ')
        message('You entered {} {} {} {} '.format(saleitemid, salequantity, saletotal, showid))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.ADD
    sale = Sales(saleitemid, salequantity, saletotal, showid, update_ind)
    g.sales_list.append(sale)

    for sale in g.sales_list:
        message(sale)


def modify_show_info():
    pass

def delete_show_info():
    pass

def show_all_info():
    '''This function will display all database records to the user'''

    message('###########  Artists Records  ############')
    for arty in g.artists_list:
        message(arty)
    message('###########  Items Records  ############')
    for item in g.items_list:
        message(item)
    message('###########  Show Records  ############')
    for show in g.show_list:
        message(show)
    message('###########  Sales Records  ############')
    for sale in g.sales_list:
        message(sale)

def analyze_records():
    pass


def input_artists_info():
    '''get user information for artists in show'''
    check = ''

    while True:
        clear()
        firstname = input('Enter the first name of the artist: ')
        lastname = input('Enter the last name of the artist: ')
        message('You entered {} {} '.format(firstname, lastname))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.ADD
    art = Artists(firstname, lastname, update_ind)
    g.artists_list.append(art)

    for arty in g.artists_list:
        message(arty)
    #     message(arty.id)
    #     message(arty.firstName)
    #     message(arty.lastName)
    #     message(arty.update_ind)
    #

def input_art_items_info():
    '''get user information for items in show'''

    message('*** Here are the available Artists. One must be specified')
    message('    when adding an item.')
    for arty in g.artists_list:
        message(arty)
    message('')

    check = ''
    while True:
        clear()
        itemtype = input('Enter the type of item (e.g. print, painting, sculpture, other): ')
        itemname = input('Enter the name of the item: ')
        itemartistid = input('Enter the Artist ID from the above list: ')
        message('You entered {} {} {}  '.format(itemtype, itemname, itemartistid))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.ADD
    item = Items(itemtype, itemname, itemartistid, update_ind)
    g.items_list.append(item)

    for item in g.items_list:
        message(item)


def input_show_info():
    '''get user information about a particular show'''

    message('')
    while True:
        clear()
        showname = input('Enter the name of the Show: ')
        showlocation = input('Enter the location of the Show (city/town name): ')
        showdate = input('Enter the Show Date (YYYY-MM-DD): ')
        message('You entered {} {} {}  '.format(showname, showlocation, showdate))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.ADD
    show = Show(showname, showlocation, showdate, update_ind)
    g.show_list.append(show)

    for show in g.show_list:
        message(show)


# Clara Code
def message(msg):
    '''Display a message to the user'''
    print(msg)