def add(a, b):
    """Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """Subtracts two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The difference of a and b.
    """
    return a - b


def multiply(a, b):
    """Multiplies two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b


def divide(a, b):
    """Divides two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Raises:
        ZeroDivisionError: If b is 0.

    Returns:
        float: The quotient of a and b.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
    return a / b