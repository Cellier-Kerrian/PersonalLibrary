def even_odd(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    str
        Even or Odd.
        
    Description
    -------
        says whether n is Even or Odd.

    '''
    if (n % 2) == 0:
       return f"{n} is Even"
    else:
       return f"{n} is Odd"