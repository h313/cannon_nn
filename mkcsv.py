import xlrd
import csv
import math
import numpy as np
from pathlib import Path

WORKBOOKS_PATH = Path("xlsx")
METADATA_PATH = Path("shot_metadata.xlsx")


def read_excel(workbook):
    wb = xlrd.open_workbook(workbook)
    sheet = wb.sheet_by_index(0)
    rows = []
    for rownum in range(sheet.nrows):
        rows.append(sheet.row_values(rownum))
    return rows


def combine_data(data, metadata):
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

ALL_METADATA = read_excel(METADATA_PATH)[2:]

# Combine metadata and data rows
rows = []
for workbook in WORKBOOKS_PATH.iterdir():
    shot_number = int(workbook.name[5:-5])
    data = read_excel(workbook)[3:]
    metadata = ALL_METADATA[shot_number - 1]
    rows += combine_data(data, metadata)

# Normalize columns by highest of each one
key = []
rows = np.array(rows)
for i in range(len(rows[0])):
    highest = max(rows[:,i])
    key.append(highest)
    for row in rows:
        row[i] = row[i] / highest

# Write the rows
with open("data.csv", "w+") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(key)
    for row in rows:
        writer.writerow(row)
