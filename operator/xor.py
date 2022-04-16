def _xor(a, b):
    '''
    
    Parameters
    ----------
    a : bool
        a boolean.
    b : bool
        a boolean.

    Returns
    -------
    bool
        True or False.
        
    Description
    -------
        XOR.

    '''
    return bool((a and not b) or (not a and b))