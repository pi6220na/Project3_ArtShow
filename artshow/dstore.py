import sqlite3
import traceback
from artshow import ui, g
from artists import Artists
from artshow.items import Items
from artshow.sales import Sales
from artshow.show import Show

import logging
log = logging.getLogger(__name__)
####  example log statement:  log.info("Hello logging!")


def create_db():
    '''Create a show_db SQLite database and populate with four tables'''

    logging.info("Entering Database module")

    try:

        db = sqlite3.connect('data/show_db.db')
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")

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



    except sqlite3.Error as e:
        print('rolling back changes because of error: ' , e)
        logging.error('Database error {}'.format(e))
        traceback.print_exc()
        db.rollback()

    finally:

        db.close()


def read_db_for_records():
    ''' call four functions, one per table, to read database tables into the corresponding list '''
    g.artists_list = []
    g.items_list = []
    g.sales_list = []
    g.show_list = []
    read_db_for_artists()
    read_db_for_items()
    read_db_for_shows()
    read_db_for_sales()


def read_db_for_artists():
    '''Read show_db SQLite database and populate artists list'''
    try:

        db = sqlite3.connect('data/show_db.db')
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")

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
        logging.error('Database error {}'.format(e))
        traceback.print_exc()

    finally:
        db.close()

def read_db_for_items():
    '''Read show_db SQLite database and populate item list'''
    try:

        db = sqlite3.connect('data/show_db.db')
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")

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
        logging.error('Database error {}'.format(e))
        traceback.print_exc()

    finally:
        db.close()


def read_db_for_shows():
    '''Read show_db SQLite database and populate show list'''
    try:

        db = sqlite3.connect('data/show_db.db')
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")

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
        logging.error('Database error {}'.format(e))
        traceback.print_exc()

    finally:
        db.close()


def read_db_for_sales():
    '''Read show_db SQLite database and populate sales list'''
    try:

        db = sqlite3.connect('data/show_db.db')
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")

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
        logging.error('Database error {}'.format(e))
        traceback.print_exc()

    finally:
        db.close()



def update_records():
    update_artists()
    update_items()
    update_show()
    update_sales()


def update_artists():

    db = sqlite3.connect('data/show_db.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys=ON")

    ui.message('in update_artists')
    for artist in g.artists_list:
        ui.message(artist)

    for artist in g.artists_list:
        if artist.update_ind == g.ADD:    # add a list element to database

            try:
                with db:
                    sql = 'insert into {} values (?,?,?)'.format('artists')
                    cur.execute(sql, (None, artist.firstName, artist.lastName))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif artist.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                sql = 'update {} set FirstName = ?, LastName = ? where Artistid = ?'.format('artists')
                with db:
                    cur.execute(sql, (artist.firstName, artist.lastName, artist.id))


                #print(artist.firstName, artist.lastName, artist.id)

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif artist.update_ind == g.DELETE:      # delete list element from database

            #print(artist.id)
            #print(type(artist.id))

            try:
                sql = 'delete from {} where Artistid = ?'.format('artists')
                with db:
                    cur.execute(sql, (artist.id,))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                logging.error(traceback.print_exc())

        else:
            if artist.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()


def update_items():

    db = sqlite3.connect('data/show_db.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys=ON")

    ui.message('in update_items')
    for item in g.items_list:
        ui.message(item)

    for item in g.items_list:
        if item.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    sql = 'insert into {} values (?,?,?,?)'.format('items')
                    cur.execute(sql, (None, item.itemType, item.itemName, item.itemArtistId))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif item.update_ind == g.MODIFY:      # update a modified list element to database

            sql = 'update {} set Itemsid = ?, ItemType = ?, ItemName = ?, where ItemArtistid = ?'.format('items')
            try:

                with db:
                    cur.execute(sql, (item.id, item.itemType, item.itemName, item.itemArtistid))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif item.update_ind == g.DELETE:      # delete list element from database

            try:

                sql = 'delete from {} where Itemsid = ?'.format('items')
                with db:
                    cur.execute(sql, (item.id,))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        else:
            if item.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()


def update_show():

    db = sqlite3.connect('data/show_db.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys=ON")

    ui.message('in update_show')
    for show in g.show_list:
        ui.message(show)

    for show in g.show_list:
        if show.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    sql = 'insert into {} values (?,?,?,?)'.format('show')
                    cur.execute(sql, (None, show.showName, show.showLocation, show.showDate))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif show.update_ind == g.MODIFY:      # update a modified list element to database

            try:

                sql = 'update {} set ShowName = ?, ShowLocation = ?, ShowDate = ?, where Showid = ?'.format('show')
                with db:
                    cur.execute(sql, (show.showName, show.showLocation, show.showDate, show.id))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif show.update_ind == g.DELETE:      # delete list element from database

            try:

                sql = 'delete from {} where Showid = ?'.format('show')
                with db:
                    cur.execute(sql, (show.id,))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        else:
            if show.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()


def update_sales():

    db = sqlite3.connect('data/show_db.db')
    cur = db.cursor()
    cur.execute("PRAGMA foreign_keys=ON")

    ui.message('in update_sales')
    for sale in g.sales_list:
        ui.message(sale)

    for sale in g.sales_list:
        if sale.update_ind == g.ADD:    # add a list element to database

            try:

                with db:
                    cur.execute("PRAGMA foreign_keys=ON")
                    sql = 'insert into {} values (?,?,?,?,?)'.format('sales')
                    cur.execute(sql, (None, sale.saleItemId, sale.saleQuantity, sale.saleTotal, sale.showId))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif sale.update_ind == g.MODIFY:      # update a modified list element to database

            sql = 'update {} set SaleItemid = ?, SaleQuantity = ?, SaleTotal = ?, ' \
                  'Showid = ? where Saleid = ?'.format('sales')
            try:
                with db:
                    cur.execute(sql, (sale.saleItemId, sale.SaleQuantity, sale.SaleTotal, sale.showId, sale.id))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        elif sale.update_ind == g.DELETE:      # delete list element from database

            try:

                sql = 'delete from {} where Saleid = ?'.format('sales')
                with db:
                    cur.execute(sql, (sale.id,))

            except sqlite3.Error as e:
                print('Database error: ', e)
                logging.error('Database error {}'.format(e))
                traceback.print_exc()

        else:
            if sale.update_ind == g.BLANK: # do nothing, nothing changed in database record
                pass

    db.commit()
    db.close()
