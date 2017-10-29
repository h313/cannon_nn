#!/usr/bin/env python3
"""Puts the .csvs together into one csv, one for
training and another for testing.
"""
import csv
import sys
from pathlib import Path


def main():
    for path in ['./test', './training']:
        path = Path(path)
        print(f"Building csv for {path}")
        write_csv(build_csv(path), str(path))


def build_csv(path):
    ret = []
    for csv_file in path.glob("*.csv"):
        f = csv.reader(open(csv_file, newline=''), delimiter=",")
        for row in f:
            ret.append([row[0], row[1], row[3], row[4], row[5]])
    return sorted(ret)


def write_csv(all_csvs, file):
    csvwriter = csv.writer(open(file + '.csv', 'w', newline=''),
                            delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in all_csvs:
        csvwriter.writerow(row)


if __name__ == "__main__":
    main()