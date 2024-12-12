""" Exclusive Or

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _only one_ of the lists.

"""


def exclusive_or(str, list1, list2):
    
    """
    Checks if a given string is present in only one of two input lists.

    Args:
        item (str): The string to be searched in the lists.
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        bool: True if the item is present in only one of the lists, False otherwise.
    """
    
    return (str in list1) or (str in list2)
