# Program to load Database by Scott Suk Hoon Kim (class mate)

import sqlite3, traceback, os, sys, json
import logging
log = logging.getLogger(__name__)


''' initial setup to create table and insert intial records'''

def setup():
    dbFolder = "data"
    dbFile = os.path.join(dbFolder, "test_show_db.db")

    ''' makedirs referenced from https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist '''
    try:
        os.makedirs(dbFolder)
    except OSError as e:
        pass  # Do nothing if directory exists

    global db
    global cur

    db = sqlite3.connect(dbFile)  # Creates or opens database file
    cur = db.cursor()  # Need a cursor object to perform operations

    # Create tables if not exist
    try:
        cur.execute("PRAGMA foreign_keys=ON")

        cur.execute('CREATE TABLE IF NOT EXISTS `show` '
                    '(`Showid` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                    '`ShowName` TEXT, '
                    '`ShowLocation` TEXT, '
                    '`ShowDate` TEXT);')  # ISO8601 Date String yyyy-mm-dd format in this program
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
            print("{} error has occured".format(e))
            traceback.print_exc()  # Displays a stack trace, useful for debugging
            db.rollback()  # Optional - depends on what you are doing with the db

    # Load table values from JSON files
    ARTISTS, ITEMS, SALES, SHOW = loadRecordsFromJSON()

    # Insert/replace table values if not exist
    try:
        for artists in ARTISTS:
            cur.execute("INSERT OR REPLACE INTO 'artists' ('Artistid', 'FirstName', 'LastName') VALUES (?,?,?)",
                        [artists['Artistid'], artists['FirstName'], artists['LastName']])
        db.commit()
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc()
        db.rollback()

    # Insert/replace table values if not exist
    try:
        for item in ITEMS:
            cur.execute("INSERT OR REPLACE INTO 'items' ('Itemsid', 'ItemType', 'ItemName', 'ItemArtistid') VALUES (?,?,?,?)",
                        [item['Itemsid'], item['ItemType'], item['ItemName'], item['ItemArtistid']])
        db.commit()
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc()
        db.rollback()

    # Insert/replace table values if not exist
    try:
        for show in SHOW:
            cur.execute("INSERT OR REPLACE INTO 'show' ('Showid', 'ShowName', 'ShowLocation', 'ShowDate') VALUES (?,?,?,?)",
                        [show['Showid'], show['ShowName'], show['ShowLocation'], show['ShowDate']])
        db.commit()
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc()
        db.rollback()

    # Insert/replace table values if not exist
    try:
        for sales in SALES:
            cur.execute("INSERT OR REPLACE INTO 'sales' ('Saleid', 'SaleItemid', 'SaleQuantity', 'SaleTotal', 'Showid') VALUES (?,?,?,?,?)",
                        [sales['Saleid'], sales['SaleItemid'], sales['SaleQuantity'], sales['SaleTotal'], sales['Showid']])
        db.commit()
    except sqlite3.Error as e:
        print("{} error has occured".format(e))
        traceback.print_exc()
        db.rollback()

    #
    # # Insert/replace table values if not exist
    # try:
    #     for sqlite_master in SQLITE_MASTER:
    #         cur.execute("INSERT OR REPLACE INTO 'sqlite_master' ('type', 'name', 'tbl_name', 'rootpage', 'sql') VALUES (?,?,?,?,?)",
    #                     [sqlite_master['type'], sqlite_master['name'], sqlite_master['tbl_name'], sqlite_master['rootpage'], sqlite_master['sql']])
    #     db.commit()
    # except sqlite3.Error as e:
    #     print("{} error has occured".format(e))
    #     traceback.print_exc()
    #     db.rollback()
    #
    # # Insert/replace table values if not exist
    # try:
    #     for sqlite_sequence in SQLITE_SEQUENCE:
    #         cur.execute("INSERT OR REPLACE INTO 'sqlite_sequence' ('name', 'seq') VALUES (?,?)",
    #                     [sqlite_sequence['name'], sqlite_sequence['seq']])
    #     db.commit()
    # except sqlite3.Error as e:
    #     print("{} error has occured".format(e))
    #     traceback.print_exc()
    #     db.rollback()


def loadRecordsFromJSON():
    ''' JSON file name/path '''

    ARTISTS_FILE = os.path.join('data', 'main_artists.json')
    ITEMS_FILE = os.path.join('data', 'main_items.json')
    SALES_FILE = os.path.join('data', 'main_sales.json')
    SHOW_FILE = os.path.join('data', 'main_show.json')
    # SQLITE_MASTER = os.path.join('data', 'main_sqlite_master.json')
    # SQLITE_SEQUENCE = os.path.join('data', 'main_sqlite_sequence.json')

    try:
        with open(ARTISTS_FILE) as f:
            ARTISTS = json.load(f)
    except FileNotFoundError:
        ARTISTS = None

    try:
        with open(ITEMS_FILE) as f:
            ITEMS = json.load(f)
    except FileNotFoundError:
        ITEMS = None

    try:
        with open(SALES_FILE) as f:
            SALES = json.load(f)
    except FileNotFoundError:
        SALES = None

    try:
        with open(SHOW_FILE) as f:
            SHOW = json.load(f)
    except FileNotFoundError:
        SHOW = None

    # try:
    #     with open(SQLITE_MASTER) as f:
    #         SQLITE_MASTER = json.load(f)
    # except FileNotFoundError:
    #     SQLITE_MASTER = None
    #
    # try:
    #     with open(SQLITE_SEQUENCE) as f:
    #         SQLITE_SEQUENCE = json.load(f)
    # except FileNotFoundError:
    #     SQLITE_SEQUENCE = None

    return ARTISTS, ITEMS, SALES, SHOW #, SQLITE_MASTER, SQLITE_SEQUENCE

def main():
    loadRecordsFromJSON()
    setup()

main()