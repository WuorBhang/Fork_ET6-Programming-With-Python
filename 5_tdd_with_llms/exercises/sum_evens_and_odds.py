""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""


def sum_evens_and_odds(numbers):
    
    """
    This function takes a list of numbers and returns 
    a dictionary with sums of the even and odd numbers 
    in the list.
    
    args:
    numbers: The list of numbers to be processed.
    
    Returns:
        dict: A dictionary with two keys: "even" and "odd", 
        that each containing the sum of 
        the even and odd numbers in the list, 
        respectively.
    """
    
    
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return {"even": even_sum, "odd": odd_sum}
