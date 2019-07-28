def factorial_recursive(n: int):
    """
    Calculates factorial recursively

    :param n: argument to calculate factorial for
    :return: factorial value
    """
    if n <= 0:
        raise Exception("Can't calculate factorial for value equals or less than 0, {}".format(n))
    elif n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


def factorial_loop(n: int):
    """
    Calculates factorial in a loop

    :param n: argument to calculate factorial for
    :return: factorial value
    """
    if n <= 0:
        raise Exception("Can't calculate factorial for value equals or less than 0, {}".format(n))
    i = 1;
    result = 1;
    while i <= n:
        result *= i
        i += 1
    return result


def check_factorial(factorial, val=10):
    """
    Function to test factorial functions with user input and boundary value
    """
    print("Checking function {}, input values {}, {}".format(factorial.__name__, val, 1))
    print(factorial(val))
    print(factorial(1))


check_factorial(factorial_recursive)
check_factorial(factorial_loop)
check_factorial(factorial_recursive, 20)
# check_factorial(factorial_loop, -4)
# check_factorial(factorial_recursive, 0)
