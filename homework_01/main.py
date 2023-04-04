


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number < 2:
        return False
    for numbers in range(2, int(number ** 0.5) + 1):
        if number % numbers == 0:
            return False
    return True



def filter_numbers(numbers_list,filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    elif filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    elif filter_type == PRIME:
        return [number for number in numbers_list if is_prime(number)]
    else:
        ValueError('Invalid value, correct incoming data')