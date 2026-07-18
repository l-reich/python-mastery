import csv
import collections


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


def read_csv_as_dicts(fn: str, types: list) -> list[dict]:
    res_list = []
    with open(fn, "r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            res_list.append(
                {col: func(val) for col, func, val in zip(headers, types, row)}
            )

    return res_list


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
    Read a CSV file into a list of instances
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
