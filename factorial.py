def factorial(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    int
        decimal number.
        
    Description
    -------
        calculate the factorial of n.

    '''
    if n==1:
        return 1
    else:
        return n*factorial(n-1)