""" Helper functions for the web application. """

def cut_string(string_input, string_length):
    """ 
    Accepts a string and a numeric length, responds with a new 
    string comprised of every third character from input string

    >>> cut_string('abcdefg', 7)
    'cf'

    >>> cut_string('ab', 2)
    ''
    """

    new_string = ''

    if string_length > 2:
        for i in range(2, string_length, 3):
            new_string += string_input[i]

    return new_string