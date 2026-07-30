# reader.py

import csv
import logging

log = logging.getLogger(__name__)


def convert_csv(lines, converter, *, headers=None):
    result_list = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for line_idx, line in enumerate(rows):
        try:
            result_list.append(converter(headers, line))
        except ValueError as e:
            log.warning("Bad row: %s", line)
            log.debug("Reason : %s", e)

    return result_list


def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(
        lines,
        lambda headers, row: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
    )


def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines, lambda headers, row: cls.from_row(row))


def read_csv_as_dicts(filename, types, *, headers=None):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)


def read_csv_as_instances(filename, cls, *, headers=None):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
