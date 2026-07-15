# readrides.py

import csv
from collections import namedtuple


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            records.append(record)
    return records


def read_rides_as_named_tuples(filename):
    """
    Read the bus ride data as a list of namedtuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Record(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_cls(filename):
    """
    Read the bus ride data as a list of objects of a class with slots
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

Record = namedtuple("Record", ["route", "date", "daytype", "rides"])

class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def get_func_for_mode(mode: str):
    match mode:
        case "tup":
            f = read_rides_as_tuples
        case "dict":
            f = read_rides_as_dicts
        case "ntup":
            f = read_rides_as_named_tuples
        case "cls":
            f = read_rides_as_cls
    return f


if __name__ == "__main__":
    import tracemalloc
    import sys

    mode = sys.argv[1]
    func = get_func_for_mode(mode)

    tracemalloc.start()
    rows = func("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
