import g
# the following clear screen technique works on windows machines when running the .py file in a terminal or CMD prompt
# it does not work within the pyCharm run window and instead shows a  symbol
import os  # clear screen technique: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
clear = lambda: os.system('cls')

import logging
log = logging.getLogger(__name__)
####  example log statement:  log.info("Hello logging!")



def analyze_records():
    ''' This function will perform simple sets of analysis on the database data as stored in lists. '''

    logging.info("Entering Analysis module")

    ar_counts()
    ar_items_by_artist()
    ar_totals_by_item()
    ar_total_sales_by_artist()

    # for sales in g.sales_list:
    #     logging.info('A test of str  for printing class objects {0!s}'.format(sales))
    #     logging.info('A test of repr for printing class objects {0!r}'.format(sales))


def ar_counts():
    ''' Provides counts of each table's records on file '''
    clear()

    artist_counts = len(g.artists_list)
    items_counts = len(g.items_list)
    shows_counts = len(g.show_list)
    sales_counts = len(g.sales_list)

    print('********* Art Show Database Record Counts: *************')
    print()
    print('         Total   Artist Records: {:5}'.format(artist_counts))
    print('         Total   Item Records:   {:5}'.format(items_counts))
    print('         Total   Show Records:   {:5}'.format(shows_counts))
    print('         Total   Sales Records:  {:5}'.format(sales_counts))
    print('         =======================================')
    print('         Total   Record Count =  {:5}'.format(artist_counts+items_counts+shows_counts+sales_counts))


def ar_items_by_artist():
    ''' Simple analysis breakdown of sales by artist '''

    print()
    print('*********** Art Items Breakdown by Artist **************')
    for artists in g.artists_list:
        print()
        for item in g.items_list:
            if item.itemArtistId == artists.id:
                print('Artist ID:{:d} {:10} {:10} {}'.format((artists.id), artists.firstName, artists.lastName, str(item)))
    print()


def ar_totals_by_item():
    ''' This function will print total counts sorted by item id '''

    print()
    print('*********** Total Sales by Item ID **************')
    grandTotal = 0
    grandCount = 0
    for item in g.items_list:
        print()
        subTotal = 0
        subCount = 0
        for sale in g.sales_list:
            if sale.saleItemId == item.id:
                print('Item ID: {:d} Item Name: {:20}  {}'.format((item.id), item.itemName, str(sale)))
                subTotal = subTotal + sale.saleTotal
                subCount = subCount + 1
        print('Total for ID:{:d}  Count = {:d} Total = ${:,.2f}'.format((item.id), (subCount), (subTotal)))
        grandTotal = grandTotal + subTotal
        grandCount = grandCount + subCount
    print()
    print('Grand Total Sales = ${:12,.2f}  Total Count of all Items sold: {:d}'.format((grandTotal), (grandCount)))
    print()


def ar_total_sales_by_artist():
    ''' This function does a control break on sales records breaking on artist id '''

    print()
    print('*********** Total Sales by Artist **************')
    for artist in g.artists_list:
        totalSales = 0
        totalItems = 0
        print()
        for sale in g.sales_list:

            for item in g.items_list:
                if sale.saleItemId == item.id and item.itemArtistId == artist.id:
                    print(str('Artist ID: {:d} {:10} {:10}  {}'.format((artist.id), artist.firstName, artist.lastName, sale)))
                    totalSales = totalSales + sale.saleTotal
                    totalItems = totalItems + 1
        print('======================================================================================================')
        print('{} {}  Total Sales For All Items: ${:12,.2f} Count of all items for this artist: {:d}'
              .format(artist.firstName, artist.lastName, totalSales, totalItems))
        print()

