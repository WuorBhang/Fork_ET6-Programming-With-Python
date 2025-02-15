<<<<<<< HEAD
def mystery_1(a):
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.

    Parameters:
    a (list): A list of integers to be sorted.

    Returns:
    list: The input list sorted in ascending order.

    Examples:
    >>> mystery_1([5, 3, 8, 6, 2])
    [2, 3, 5, 6, 8]

    >>> mystery_1([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> mystery_1([10, -2, 4, 3])
    [-2, 3, 4, 10]

    >>> mystery_1([])
    []

    >>> mystery_1([9])
    [9]
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
=======
def mystery_1(a,b):
    return a + b
>>>>>>> 493fa105c419abe6ff758942e2cce0e36388e008
