def addition(a, b):
    return a + b


def addition(a, b):
    return a - b  # BUG volontaire


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b
