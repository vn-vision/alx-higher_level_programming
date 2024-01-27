#!/usr/bin/python3
''' add_integer - adds two integers '''


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number. Defaults to None.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """

    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
