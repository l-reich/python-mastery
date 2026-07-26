import csv
import collections
from abc import ABC, abstractmethod


class DataCollection(collections.abc.Sequence):
    def __init__(self, column_names):
        self.col_dict = {name: [] for name in column_names}
        self.col_names = column_names

    def __getitem__(self, index):
        return {
            col_key: self.col_dict[col_key][index] for col_key in self.col_dict.keys()
        }

    def __len__(self):
        example_key = self.col_names[0]
        return len(self.col_dict[example_key])

    def append(self, d):
        for k in self.col_dict.keys():
            self.col_dict[k].append(d[k])


class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


def read_csv_as_dicts(filename: str, types: list) -> list[dict]:
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types)


def read_csv_as_columns(fn: str, types: list) -> DataCollection:
    with open(fn, "r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data_coll = DataCollection(headers)
        for row in reader:
            data_coll.append(
                {col: func(val) for col, func, val in zip(headers, types, row)}
            )

    return data_coll


def read_csv_as_instances(filename, cls):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls)

def csv_as_dicts(file, types: list):
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records

def csv_as_instances(file, cls):
    """
    Read CSV data into a list of instances
    """
    records = []
    rows = csv.reader(file)
    _ = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
