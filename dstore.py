import sqlite3
import traceback
import g, ui
from artists import Artists
from items import Items
from sales import Sales
from show import Show



def add_art_items_record():
    pass


def add_show_record():
    pass


def get_data():


    name = input('Enter the name of the juggler: ')
    country = input('Enter the country of the juggler: ')
    catches = int(input('Enter the number of catches the juggle made: '))

    return name, country, catches


def add_to_db(cur, db, name, country, catches):

    try:
        with db:
            cur.execute('insert into juggler values (?,?,?)', (name, country, catches))

    except sqlite3.Error as e:
        print('Database error: ', e)
        traceback.print_exc()

    finally:

        return cur, db


def update_juggler(cur, db):

    name_in = input('Enter the name of the juggler to update: ')
    catches_in = int(input('Enter the correct number of catches: '))

    try:
        with db:
            cur.execute('update juggler set catches = ? where name = ?', (catches_in, name_in))

    except sqlite3.Error as e:
        print('Database error: ', e)
        traceback.print_exc()


def delete_juggler(cur, db):

    ui.message('')
    inp_name = input('Enter the name of the juggler: ')

    try:
        with db:
            cur.execute('delete from juggler where name = ?', (inp_name,))

    except sqlite3.Error as e:
        print('Database error: ', e)
        traceback.print_exc()


def print_db(cur, db):

    ui.message('')
    try:
        for row in cur.execute('select * from juggler'):
            print(row)

    except sqlite3.Error as e:
        print('Database error: ', e)
        traceback.print_exc()


def create_db():
    '''Create a show_db SQLite database and populate with four tables'''
    try:

        db = sqlite3.connect('show_db.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS `show` '
                    '(`Showid` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                    '`ShowName` TEXT, '
                    '`ShowLocation` TEXT, '
                    '`ShowDate` TEXT);')                # ISO8601 Date String yyyy-mm-dd format in this program
        cur.execute('CREATE TABLE IF NOT EXISTS `artists`'
                    '(`Artistid` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                    '`FirstName` TEXT,'
                    '`LastName`	TEXT);')
        cur.execute('CREATE TABLE IF NOT EXISTS `items` '
                    '(`Itemsid`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                    '`ItemType`	TEXT,'
                    '`ItemName`	TEXT,'
                    '`ItemArtistid`	INTEGER NOT NULL , FOREIGN KEY(`ItemArtistid`) REFERENCES `artists`(`Artistid`));')
        cur.execute('CREATE TABLE IF NOT EXISTS `sales` '
                    '(`Saleid` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                    '`SaleItemid` INTEGER NOT NULL ,'
                    '`SaleQuantity` INTEGER,'
                    '`SaleTotal` NUMERIC,'
                    '`Showid` INTEGER NOT NULL, FOREIGN KEY(`Showid`) REFERENCES `show`(`Showid`),'
                     'FOREIGN KEY(`SaleItemid`) REFERENCES `items`(`Itemsid`));')
        cur.execute("PRAGMA foreign_keys=ON")


    except sqlite3.Error as e:
        print('rolling back changes because of error: ' , e)
        traceback.print_exc()
        db.rollback()

    finally:

        db.close()


def read_db_for_artists():
    '''Read show_db SQLite database and populate artists list'''
    try:

        db = sqlite3.connect('show_db.db')
        cur = db.cursor()

        # Fetch some data, using the cursor. This returns another cursor object
        # that can be iterated over
        for row in cur.execute('select * from artists'):
            #ui.message(row)
            update_ind = g.BLANK
            art = Artists(row[1], row[2], update_ind)
            art.set_id(row[0])
            g.artists_list.append(art)

        # ui.message('************* Artists **************')
        # ui.message(g.artists_list)
        # ui.message('')

    except sqlite3.Error as e:
        # As we are reading, no changes to roll back
        print('Error reading from database', e)
        traceback.print_exc()

    finally:
        db.close()

def read_db_for_items():
    '''Read show_db SQLite database and populate item list'''
    try:

        db = sqlite3.connect('show_db.db')
        cur = db.cursor()

        # Fetch some data, using the cursor. This returns another cursor object
        # that can be iterated over
        for row in cur.execute('select * from items'):
            #ui.message(row)
            update_ind = g.BLANK
            item = Items(row[1], row[2], row[3], update_ind)
            item.set_id(row[0])
            g.items_list.append(item)

        # ui.message('************* Items **************')
        # ui.message(g.items_list)
        # ui.message('')

    except sqlite3.Error as e:
        # As we are reading, no changes to roll back
        print('Error reading from database', e)
        traceback.print_exc()

    finally:
        db.close()


def read_db_for_shows():
    '''Read show_db SQLite database and populate show list'''
    try:

        db = sqlite3.connect('show_db.db')
        cur = db.cursor()

        # Fetch some data, using the cursor. This returns another cursor object
        # that can be iterated over
        for row in cur.execute('select * from show'):
            #ui.message(row)
            update_ind = g.BLANK
            show = Show(row[1], row[2], row[3], update_ind)
            show.set_id(row[0])
            g.show_list.append(show)

        # ui.message('************* Shows **************')
        # ui.message(g.show_list)
        # ui.message('')

    except sqlite3.Error as e:
        # As we are reading, no changes to roll back
        print('Error reading from database', e)
        traceback.print_exc()

    finally:
        db.close()


def read_db_for_sales():
    '''Read show_db SQLite database and populate sales list'''
    try:

        db = sqlite3.connect('show_db.db')
        cur = db.cursor()

        # Fetch some data, using the cursor. This returns another cursor object
        # that can be iterated over
        for row in cur.execute('select * from sales'):
            #ui.message(row)
            update_ind = g.BLANK
            sales = Sales(row[1], row[2], row[3], row[4], update_ind)
            sales.set_id(row[0])
            g.sales_list.append(sales)

        # ui.message('************* Sales **************')
        # ui.message(g.sales_list)
        # ui.message('')

    except sqlite3.Error as e:
        # As we are reading, no changes to roll back
        print('Error reading from database', e)
        traceback.print_exc()

    finally:
        db.close()


def update_artists():

    db = sqlite3.connect('show_db.db')
    cur = db.cursor()

    ui.message('in update_artists')
    for artist in g.artists_list:
        ui.message(artist)

    for artist in g.artists_list:
        if artist.update_ind == g.ADD:    # add a list element to database

            try:
                with db:
                    cur.execute('insert into artists values (?,?,?)', (None, artist.firstName, artist.lastName))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif artist.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                with db:
                    cur.execute('update artists set artists.FirstName = ?, artists.LastName = ? '
                                'where artists.Artistid = ?', (artist.firstName, artist.lastName, artist.id))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif artist.update_ind == g.DELETE:      # delete list element from database

            try:

                with db:
                    cur.execute('delete from artists where artists.Artistid = ?', artist.id)

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        else:
            if artist.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass


    db.commit()
    db.close()


def update_items():

    db = sqlite3.connect('show_db.db')
    cur = db.cursor()

    ui.message('in update_items')
    for item in g.items_list:
        ui.message(item)

    for item in g.items_list:
        if item.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    cur.execute('insert into items values (?,?,?,?)',
                               (None, item.itemType, item.itemName, item.itemArtistId))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif item.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                with db:
                    cur.execute('update items set items.Itemsid = ?, items.ItemType = ?, items.ItemName = ? '
                                'where items.ItemArtistid = ?',
                                (item.id, item.itemType, item.itemName, item.itemArtistid))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif item.update_ind == g.DELETE:      # delete list element from database

            try:

                with db:
                    cur.execute('delete from items where items.Itemsid = ?', item.id)

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        else:
            if item.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()


def update_show():

    db = sqlite3.connect('show_db.db')
    cur = db.cursor()

    ui.message('in update_show')
    for show in g.show_list:
        ui.message(show)

    for show in g.show_list:
        if show.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    cur.execute('insert into show values (?,?,?,?)',
                               (None, show.showName, show.showLocation, show.showDate))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif show.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                with db:
                    cur.execute('update show set show.ShowName = ?, show.ShowLocation = ?, show.ShowDate = ?'
                                'where show.Showid = ?',
                                (show.showName, show.showLocation, show.showDate, show.id))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif show.update_ind == g.DELETE:      # delete list element from database

            try:

                with db:
                    cur.execute('delete from show where show.Showid = ?', show.id)

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        else:
            if show.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()


def update_sales():

    db = sqlite3.connect('show_db.db')
    cur = db.cursor()

    ui.message('in update_sales')
    for sale in g.sales_list:
        ui.message(sale)

    for sale in g.sales_list:
        if sale.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    cur.execute('insert into sales values (?,?,?,?,?)',
                               (None, sale.saleItemId, sale.saleQuantity, sale.saleTotal, sale.showId))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif sale.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                with db:
                    cur.execute('update sales set sales.SaleItemid = ?, sales.SaleQuantity = ?, '
                                'sales.SaleTotal = ?, sales.Showid = ?'
                                'where sales.Saleid = ?',
                                (sale.saleItemId, sale.SaleQuantity, sale.SaleTotal, sale.sale.Showid, sale.Saleid))

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        elif sale.update_ind == g.DELETE:      # delete list element from database

            try:

                with db:
                    cur.execute('delete from sales where sales.Saleid = ?', sale.Saleid)

            except sqlite3.Error as e:
                print('Database error: ', e)
                traceback.print_exc()

        else:
            if sale.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()
