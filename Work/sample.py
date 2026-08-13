from logcall import logformat
from validate import Integer, validated


@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y


@validated
def sub(x: Integer, y: Integer) -> Integer:
    return x - y


@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x**y


@logformat("{func.__code__.co_filename}:{func.__name__}")
def mul(x, y):
    return x * y
