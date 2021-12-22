def binary_decimal(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    str
        a binary number.
        
    Descrition
    -------
        returns the binary number of a decimal number.

    '''
    
    if n==1:
        return "1"
    else:
        return str(binary_decimal(n//2))+str(n%2)