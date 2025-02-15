""" Repeat Character

Write a function that takes in a string, a single character, and a number. 
The function returns a string with each occurrence of the character repeated n times.

"""
<<<<<<< HEAD


def repeat_character(string, char, n):
    """_summary_
    This function will takes in a string, a single character, and a number
    and returns a string with each appearance
    of the character repeated n times.

    Args:
        string (str):The input string to be processed.
        char (char):The character to be repeated.
        n (int): The number of times the character should be repeated. It is an integer.

    Returns:
        str: The input string with each appearance of the character repeated n times.
    """

    if n == 0:
        return string
    else:
        return string.replace(char, char * n)
=======
>>>>>>> 493fa105c419abe6ff758942e2cce0e36388e008
