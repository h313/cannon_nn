import xlrd
import csv
import os


def csv_from_excel(workbook):
    wb = xlrd.open_workbook('xlsx/' + workbook)
    sh = wb.sheet_by_name(workbook[:6])
    csv_file = open(workbook[:7] + '.csv', 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()


for filename in os.listdir('./xlsx/'):
    if filename[-5:] == '.xlsx':
        print(filename)
        csv_from_excel(filename)
