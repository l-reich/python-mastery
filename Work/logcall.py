from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("calling", function.__name__)
        return function(*args, **kwargs)

    return wrapper


def logformat(fmt):
    def logged(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=function))
            return function(*args, **kwargs)

        return wrapper

    return logged
