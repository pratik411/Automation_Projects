import xlrd, unittest
from ddt import ddt, data, unpack

def get_data(filename,temp):

    rows = []
    # create an empty list to store rows
    book = xlrd.open_workbook(filename)
    # open the specified Excel spreadsheet as workbook
    sheet = book.sheet_by_index(0)
    # get the first sheet
    print'No of filled Rows in File :',sheet.nrows
    print'No of filled Columns in File :',sheet.ncols

    # iterate through the sheet and get data from rows in list
    # here we have taken range from 1, so it would skip 1st row and start taking value form next row.
    #for row_idx in range(temp, sheet.nrows):
    row_idx = temp
    rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    print "Row index number :" ,row_idx
    a = sheet.row_values(row_idx, 0, sheet.ncols)
        #print list(sheet.row_values(row_idx, 0, sheet.ncols))

    return a

