from decorators import unique_elements_decorator

@unique_elements_decorator
def get_sample_list():
    return [1, 2, 2, 3, 4, 4, 5, 1, 3, "apple", "banana", "apple"]

if __name__ == "__main__":
    print("Результат:", get_sample_list())
