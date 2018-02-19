'''
Project 3 - Tour Merchandise Manager
concept adapted to handle an artist selling artwork at art shows
Jeremy Wolfe
MCTC ITEC Capstone 2905-01 Spring 2018

Description: This program uses the SQLite Database Python engine to store user input data containing
information for art work items sold at art shows. A command line interface is used to allow
the user to enter data, modify data, delete data, and perform analysis on show sales.

At the start of the program, all database records are read into their corresponding list structure.
All processing is then performed on the lists.
As the element lists are updated, the lists are iterated through and the database is updated according
to each list element's update-ind (add, modify, delete, blank(do nothing)).

Simple analysis functions are available to format the information based on the data relationships.
E.g. The Sales record/element contains pointers (integer id's) to other records/elements. These relationships
are enforced on the database via foreign key constraint enforcement.

Info and Error level logging entries are made and logged to artShow.log

'''
import analysis
from artshow import ui, dstore
import logging
import logging.config
#logging.basicConfig(filename='artshow.log', level=logging.INFO)

def main():

    #log = logging.getLogger(__name__)
    #log.info("Hello logging!")

    logging.config.fileConfig("logs/log.conf")

    logging.debug("Starting main program show_manager.py")
    logging.debug("1")          # test logging level
    logging.info("2")           # test logging level
    logging.warning("3")        # test logging level
    logging.error("4")          # test logging level
    logging.critical("5")       # test logging level

    dstore.create_db()  # create database and table juggler

    # read database tables and populate corresponding global lists
    dstore.read_db_for_records()

    # show all elements in the lists
    ui.show_all_info()

    while True:
        choice = ui.print_main_menu()

        # add information for Artists, Items, and Shows to their corresponding type List.
        if choice == '1':

            choice_1 = ui.add_show_info()
            if choice_1 == '1':
                ui.input_artists_info()
            elif choice_1 == '2':
                ui.input_art_items_info()
            elif choice_1 == '3':
                ui.input_show_info()
            elif choice_1 == 'q':
                choice = ui.print_main_menu()

            # cycle through all of the data lists and add/update database tables accordingly
            dstore.update_records()
            dstore.read_db_for_records()

        # sales records input separately because of dependencies on the other three record table types
        if choice == '2':

            ui.add_sales_record()
            dstore.update_records()
            dstore.read_db_for_records()

        # modify information for Artists, Items, Shows, and Sales in their corresponding type List.
        if choice == '3':
            ui.modify_show_info()
            dstore.update_records()
            dstore.read_db_for_records()

        # display the data in all four lists/database table types
        if choice == '4':
            ui.show_all_info()

        # perform some simple analysis functions on the database objects as stored in lists.
        if choice == '5':
            analysis.analyze_records()

        if choice == 'q':
            logging.debug("Quiting Program Normally")
            break   # break out of while loop and exist program

main()

