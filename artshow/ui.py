from artists import Artists
from items import Items
from sales import Sales
from show import Show
import g

import logging
import logging.config
log = logging.getLogger(__name__)

# the following clear screen technique works on windows machines when running the .py file in a terminal or CMD prompt
# it does not work within the pyCharm run window and instead shows a  symbol
import os  # clear screen technique: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
clear = lambda: os.system('cls')


def print_main_menu():
    #clear()

    logging.info("Entering UI - User Interface module")

    valid = False
    choice = ''

    message('********** Welcome to the Art Show Database Program ***********')
    message('')
    message('1) Add show info: Artists, Items, and Shows')
    message('2) Add a Sales record for a Show')
    message('3) Modify/Delete a Record: Artists, Items, Shows, and Sales')
    message('4) Show Info: Artists, Items, Shows, and Sales')
    message('5) Analysis on Records')
    message('"q" to quit the program')
    message('')

    while not valid:

        choice = input('Enter 1, 2, 3, 4, or 5 or q: ')
        if (choice != '1' and choice != '2' and choice != '3' and choice != '4'
                and choice != '5' and choice != 'q'):
            print('Error, please enter 1, 2, 3, 4, or 5 or q to quit: ')
            logging.info('The user made an input value error.')
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
            logging.info('The user made an input value error.')
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

        while True:
            try:
                saleitemid = int(input('Enter the item ID of the sale item (an integer from above list): '))
                if saleitemid < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        while True:
            try:
                salequantity = int(input('Enter the quantity of sales items sold: '))
                if salequantity < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        while True:
            try:
                saletotal = float(input('Enter the total sale dollar amount: '))
                if saletotal < 0:
                    message('Enter a positive amount')
                else:
                    break
            except ValueError:
                message('Enter a whole decimal number')
        while True:
            try:
                showid = int(input('Enter the Show ID (an integer from the above list): '))
                if showid < 0:
                    message('Enter a positive amount')
                else:
                    break
            except ValueError:
                message('Enter a whole number')

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
    '''This function will allow the user to change/update/delete any record'''
    clear()

    valid = False
    choice = ''

    message('')
    message('  Update/Delete Show Information')
    message('1) Artists Record')
    message('2) Art Items Record')
    message('3) Shows Record')
    message('4) Sales Record')
    message('"q" to return to main menu')
    message('')

    while not valid:

        choice = input('Enter 1, 2, 3, 4, or q: ')
        if (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != 'q'):
            message('Error, please enter 1, 2, 3, 4, or q to return: ')
            logging.info('The user made an input value error.')
        else:
            valid = True

    if choice == '1':
        update_artists_record()
    elif choice == '2':
        update_items_record()
    elif choice == '3':
        update_shows_record()
    elif choice == '4':
        update_sales_record()
    else:
        return


def update_artists_record():
    '''This function will update or delete an artists record from the artists_list list'''

    clear()
    message('')
    message('*** Here are the available Artists. ')
    for art in g.artists_list:
        message(art)
    message('')

    artist_index = 0
    artist_id = 0
    valid = False
    while True:
        while True:
            try:
                choiceNum = int(input('Please specify the artist record id you want to modify: '))
                if choiceNum < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')

        for idx, art in enumerate(g.artists_list):
            #print(idx, art)
            if art.id == choiceNum:
                #print(art.id, choiceNum)
                valid = True
                artist_index = int(idx)
                artist_id = art.id

        if valid:
            mod_type = input('Modify the record or Delete the record? Input "m" or "d":' )
            if mod_type.lower() == 'm':
                modify_artists_record(artist_index, artist_id)
            elif mod_type.lower() == 'd':
                delete_artists_record(artist_index)

            break


def modify_artists_record(artist_index, artist_id):

    print('Your record to modify is:')
    print(g.artists_list[artist_index])

    while True:
        clear()
        firstname = input('re-enter the first name of the artist: ')
        lastname = input('re-enter the last name of the artist: ')
        message('You entered {} {} '.format(firstname, lastname))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    #junk = g.artists_list.pop([artist_index])     # remove the old element
    update_ind = g.MODIFY
    art = Artists(firstname, lastname, update_ind)  # generate a new replacement object
    art.set_id(artist_id)
    g.artists_list.insert(artist_index, art)        # insert the object back into the list where it came from

    print('added artist record back into list')
    print(art)


def delete_artists_record(artist_index):
    ''' pop item object off of list, change update_ind to DELETE and replace back into list '''

    temp = g.artists_list.pop(artist_index)
    temp.update_ind = g.DELETE
    g.artists_list.append(temp)


def update_items_record():
    '''This function will update or delete an item record from the items_list list'''

    clear()
    message('')
    message('*** Here are the available Items. ')
    for item in g.items_list:
        message(item)
    message('')

    item_index = 0
    item_id = 0
    valid = False
    while True:
        while True:
            try:
                choiceNum = int(input('Please specify the record item id you want to modify: '))
                if choiceNum < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')

        for idx, item in enumerate(g.items_list):
            #print(idx, item)
            if item.id == choiceNum:
                #print(item.id, choiceNum)
                valid = True
                item_index = int(idx)
                item_id = item.id

        if valid:
            mod_type = input('Modify the record or Delete the record? Input "m" or "d":')
            if mod_type.lower() == 'm':
                modify_items_record(item_index, item_id)
            elif mod_type.lower() == 'd':
                delete_items_record(item_index)

            break


def modify_items_record(item_index, item_id):
    print('Your record to modify is:')
    print(g.items_list[item_index])

    while True:
        clear()
        itemtype = input('Enter the type of item (e.g. print, painting, sculpture, other): ')
        itemname = input('Enter the name of the item: ')
        while True:
            try:
                itemartistid = int(input('Enter the Artist ID from the above list: '))
                if itemartistid < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        message('You entered {} {} {}  '.format(itemtype, itemname, itemartistid))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.MODIFY
    item = Items(itemtype, itemname, itemartistid, update_ind)  # generate a new replacement object
    item.set_id(item_id)
    g.items_list.insert(item_index, item)  # insert the object back into the list where it came from

    for item in g.items_list:
        message(item)


def delete_items_record(item_index):
    ''' pop item object off of list, change update_ind to DELETE and replace back into list '''

    temp = g.items_list.pop(item_index)
    temp.update_ind = g.DELETE
    g.items_list.append(temp)


def update_shows_record():
    '''This function will update or delete an item record from the show_list list'''

    clear()
    message('')
    message('*** Here are the available Shows. ')
    for show in g.show_list:
        message(show)
    message('')

    show_index = 0
    show_id = 0
    valid = False
    while True:
        while True:
            try:
                choiceNum = int(input('Please specify the record Show id you want to modify: '))
                if choiceNum < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')

        for idx, show in enumerate(g.show_list):
            #print(idx, show)
            if show.id == choiceNum:
                #print(show.id, choiceNum)
                valid = True
                show_index = int(idx)
                show_id = show.id

        if valid:
            mod_type = input('Modify the record or Delete the record? Input "m" or "d":')
            if mod_type.lower() == 'm':
                modify_shows_record(show_index, show_id)
            elif mod_type.lower() == 'd':
                delete_shows_record(show_index)

            break


def modify_shows_record(show_index, show_id):
    print('Your record to modify is:')
    print(g.show_list[show_index])

    while True:
        clear()
        showname = input('Enter the name of the Show: ')
        showlocation = input('Enter the location of the Show (city/town name): ')
        showdate = input('Enter the Show Date (YYYY-MM-DD): ')
        message('You entered {} {} {}  '.format(showname, showlocation, showdate))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.MODIFY
    show = Show(showname, showlocation, showdate, update_ind)  # generate a new replacement object
    show.set_id(show_id)
    g.show_list.insert(show_index, show)  # insert the object back into the list where it came from

    for item in g.show_list:
        print(item)


def delete_shows_record(show_index):
    ''' pop item object off of list, change update_ind to DELETE and replace back into list '''

    temp = g.show_list.pop(show_index)
    temp.update_ind = g.DELETE
    g.show_list.append(temp)


def update_sales_record():
    '''This function will update or delete an sales record from the sales_list list'''

    clear()
    message('')
    message('*** Here are the available Sales. ')
    for sale in g.sales_list:
        message(sale)
    message('')

    sale_index = 0
    sale_id = 0
    valid = False
    while True:
        while True:
            try:
                choiceNum = int(input('Please specify the record Sale id you want to modify: '))
                if choiceNum < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')

        for idx, sale in enumerate(g.sales_list):
            #print(idx, sale)
            if sale.id == choiceNum:
                #print(sale.id, choiceNum)
                valid = True
                sale_index = int(idx)
                sale_id = sale.id

        if valid:
            mod_type = input('Modify the record or Delete the record? Input "m" or "d":')
            if mod_type.lower() == 'm':
                modify_sales_record(sale_index, sale_id)
            elif mod_type.lower() == 'd':
                delete_sales_record(sale_index)

            break


def modify_sales_record(sale_index, sale_id):
    print('Your record to modify is:')
    print(g.sales_list[sale_index])

    while True:
        clear()

        while True:
            try:
                saleitemid = int(input('Enter the item ID of the sale item (an integer from above list): '))
                if saleitemid < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        while True:
            try:
                salequantity = int(input('Enter the quantity of sales items sold: '))
                if salequantity < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        while True:
            try:
                saletotal = float(input('Enter the total sale dollar amount: '))
                if saletotal < 0:
                    message('Enter a positive amount')
                else:
                    break
            except ValueError:
                message('Enter a positive amount')
        while True:
            try:
                showid = int(input('Enter the Show ID (an integer from the above list): '))
                if showid < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
        message('You entered {} {} {} {} '.format(saleitemid, salequantity, saletotal, showid))
        check = input('Is this correct? "y" or "n": ')
        if check.lower() == 'y':
            break

    update_ind = g.MODIFY
    sale = Sales(saleitemid, salequantity, saletotal, showid, update_ind)  # generate a new replacement object
    sale.set_id(sale_id)
    g.sales_list.insert(sale_index, sale)  # insert the object back into the list where it came from


def delete_sales_record(sale_index):
    ''' pop item object off of list, change update_ind to DELETE and replace back into list '''

    temp = g.sales_list.pop(sale_index)
    temp.update_ind = g.DELETE
    g.sales_list.append(temp)


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
        while True:
            try:
                itemartistid = int(input('Enter the Artist ID from the above list: '))
                if itemartistid < 0:
                    message('Enter a positive number')
                else:
                    break
            except ValueError:
                message('Enter a whole number')
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