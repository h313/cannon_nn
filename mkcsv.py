"""
Combines all shot data excel spreadsheets and shot conditions into
a huge csv creatively named data.csv
"""

import xlrd
import csv
import math
import numpy as np
from pathlib import Path

WORKBOOKS_PATH = Path("xlsx")
METADATA_PATH = Path("shot_metadata.xlsx")


def read_excel(workbook):
    """
    Reads an excel file (workbook) into a 2D array
    """
    wb = xlrd.open_workbook(workbook)
    sheet = wb.sheet_by_index(0)
    rows = []
    for rownum in range(sheet.nrows):
        rows.append(sheet.row_values(rownum))
    return rows


def combine_data(data, metadata):
    """
    Combines shot metadata (charge mass and shot mass) with each
    row of the actual data (time, velocity, distance)
    """
    charge_mass = metadata[1]
    shot_mass = metadata[2]

    combined = []
    for row in data:
        time = row[0]
        velocity = row[1]
        x = row[4]
        y = row[5]
        slant = row[6]

        r = math.sqrt(x**2 + y**2 + slant**2)
        combined.append([time, charge_mass, shot_mass, velocity, r])
    return combined

ALL_METADATA = read_excel(METADATA_PATH)[2:] # first two rows are units

# Combine metadata and data rows
rows = []
for workbook in WORKBOOKS_PATH.iterdir():
    shot_number = int(workbook.name[5:-5])
    data = read_excel(workbook)[3:] # first 3 rows are units
    metadata = ALL_METADATA[shot_number - 1]
    rows += combine_data(data, metadata)

# Normalize columns by dividing by the highest of each one (including time)
biggest = []
rows = np.array(rows)
for i in range(len(rows[0])):
    highest = max(rows[:,i])
    biggest.append(highest)
    for row in rows:
        row[i] = row[i] / highest

# Write the rows
with open("data.csv", "w+") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(biggest)
    for row in rows:
        writer.writerow(row)
