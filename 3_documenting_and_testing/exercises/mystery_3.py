def mystery_3(a: list, b: list = None) -> list:
    """
    Sorts a list of integers in ascending order using a manual implementation of Selection Sort.

    Parameters:
    a (list): A list of integers to be sorted.
    b (list, optional): A list to store the sorted elements. Defaults to an empty list.

    Returns:
    list: A new list containing the elements of `a`, sorted in ascending order.

    Examples:
    >>> mystery_3([5, 3, 8, 6, 2])
    [2, 3, 5, 6, 8]

    >>> mystery_3([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> mystery_3([10, -2, 4, 3])
    [-2, 3, 4, 10]

    >>> mystery_3([])
    []

    >>> mystery_3([9])
    [9]
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
