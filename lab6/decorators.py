
def unique(func):
    def wrapper():
        result = func()
        return list(set(result))
    return wrapper
