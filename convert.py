#!/usr/bin/env python3
"""Convert Excel (xlsx) workbooks into CSV files for simpler parsing
This should be used from the command line. Some possibilities:

    $ ./convert.py training
    $ ./convert.py test
    $ ./convert.py training test

The command line tool assumes all xlsx files are located in a `xlsx` subdirectory
within each specified directory. It outputs generated CSVs in the root of the
specified directories:

    training
    ├── Skott1.csv
    ├── Skott10.csv
    └── xlsx
        ├── Skott1.xlsx
        └── Skott10.xlsx

Note that this tool will overwrite any existing CSVs in the directory!
"""
import xlrd
import csv
import sys
from pathlib import Path


def main(paths):
    if len(paths) == 0:
        print("Please specify paths as command line arguments")
        return
    for path in paths:
        path = Path(path)
        print(f"Converting {path}")
        convert_directory(path)


def csv_from_excel(workbook):
    wb = xlrd.open_workbook(workbook)
    sheet = wb.sheet_by_index(0)
    csv_file = workbook.parents[1] / (workbook.stem + ".csv")
    with csv_file.open("w+") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sheet.nrows):
            writer.writerow(sheet.row_values(rownum))


def convert_directory(path):
    workbooks = path / "xlsx"
    for workbook in workbooks.glob("*.xlsx"):
        csv_from_excel(workbook)


if __name__ == "__main__":
    main(sys.argv[1:])
