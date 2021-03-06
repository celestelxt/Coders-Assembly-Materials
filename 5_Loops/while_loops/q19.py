import random

def get_invalid_entries(guess):
    """ Returns the non-valid characters 

        The possible valid characters are:
            'R', 'Y', 'B', 'O', 'G', 'V'. 
        (R: Red, Y: Yellow, B: Blue, O: Orange, G: Green, V: Violet)
        
        All other characters are considered invalid.

        For example, get_invalid_entries('ABCD') returns 'ACD'
        
        Returns: the invalid characters(type: str)
    """
    COLORS = 'RYBOGV'
    return None

def generate_secret_code():
    """ Generates a secret code of length 4

        The code will consists of the following character 
        'R', 'Y', 'B', 'O', 'G', 'V', 
        each representing a color. 
        (R: Red, Y: Yellow, B: Blue, O: Orange, G: Green, V: Violet)
        
        Each color can be repeated for 2 or more times.

        Returns: the color code (type: str)
    """
    return None


def count_exact_matches(guess, code):
    """ Count the number the exact match of characters at 
        the same index in guess and code

        Parameters:
            guess (type: str): the guess inputted by the player
            code (type: str): the secret code generated by the computer

        Returns: the count of exact matches (type: int)
    """
    return None

def count_partial_matches(guess, code):
    """ Count the number the partial match of characters 
        (right color but at the wrong position)

    Parameters:
        guess (type: str): the guess inputted by the player
        code (type: str): the secret code generated by the computer

    Returns: the count of partial matches (type: int)
    """
    return None

