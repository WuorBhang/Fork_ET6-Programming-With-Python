<<<<<<< HEAD
def mystery_2(a: list, b: int) -> list:
    """
    Filters a list `a` to include only elements containing the integer `b`.

    Parameters:
    a (list): A list of integers or sublists of integers to be filtered.
    b (int): An integer to check within each element of `a`.

    Returns:
    list: A new list containing elements from `a` where `b` is found.

    Examples:
    >>> mystery_2([[1, 2, 3], [4, 5], [3, 6, 7]], 3)
    [[1, 2, 3], [3, 6, 7]]

    >>> mystery_2([123, 456, 789], 4)
    [456]

    >>> mystery_2([], 3)
    []

    >>> mystery_2([[1, 2], [3, 4], [5, 6]], 7)
    []

    >>> mystery_2([10, 20, 30, 40], 20)
    [20]
    """
    c = []
    while a:
        if b in a[0] if isinstance(a[0], list) else str(b) in str(a[0]):
            c.append(a[0])
        a = a[1:]
    return c
=======
def mystery_2(a):
    if len(a) == 0:
        return None

    return len(a)
>>>>>>> 493fa105c419abe6ff758942e2cce0e36388e008
