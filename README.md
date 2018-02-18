# Project3_ArtShow
MCTC ITEC 2905-01 Capstone - Project 3 - Tour Merchandise Manager (Art Show)

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

Database Tables:
    artists - artist name
    items - type, item name, artist id
    show - show name, location, date
    sales - item id, sale quantity, sale total, show id
    
Modules:
    analysis.py - option 5 main menu - perform analysis on objects in table lists
    dstore.py - database functions
    show_manager.py - main control module
    ui.py - user interface module - bulk of program logic in here
    
Classes:
    artists.py
    items.py
    sales.py
    show.py
    
Global container:
    g.py
  
Database:
    show_db.db
    
Logging:
    artShow.log - example log file
    log.conf - logging configuration file
   
