def logged(function):
    def wrapper(*args, **kwargs):
        print("calling", function.__name__)
        return function(*args, **kwargs)

    return wrapper
