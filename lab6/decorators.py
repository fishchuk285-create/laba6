def unique_elements_decorator(func):
    """Декоратор, який залишає у повернутому списку лише унікальні елементи."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return list(set(result))
        return result
    return wrapper
