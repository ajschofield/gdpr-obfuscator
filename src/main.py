import csv
from io import StringIO
from typing import List, Dict

def csv_reader(content: str) -> List[Dict[str, str]]:
    f = StringIO(content)
    reader = csv.DictReader(f)
    return list(reader)
