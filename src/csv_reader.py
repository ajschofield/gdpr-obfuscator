import csv
from io import StringIO

def csv_reader(file):
    f = StringIO(file)
    reader = csv.DictReader(f)
    return list(reader)
