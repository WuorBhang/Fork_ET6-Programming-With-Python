def mystery_4(a: list[int], b: int) -> list[int]:
    """
    Filters a list `a` to include only integers that are equal to `b`.

    Parameters:
    a (list[int]): A list of integers to be filtered.
    b (int): An integer value to check for in the list `a`.

    Returns:
    list[int]: A new list containing only the elements in `a` that match `b`.

    Examples:
    >>> mystery_4([1, 2, 3, 4, 2, 5], 2)
    [2, 2]

    >>> mystery_4([10, 20, 30, 40], 15)
    []

    >>> mystery_4([5, 5, 5, 5], 5)
    [5, 5, 5, 5]

    >>> mystery_4([], 1)
    []

    >>> mystery_4([1, 2, 3, 4, 5], 6)
    []
    """
    c = []
    for d in a:
        if d == b:
            c.append(d)
    return c
