def longueur(c):
    '''

    Parameters
    ----------
    c : list/dict/str
        the element from which we calculate len().

    Returns
    -------
    nbr_element
        number of element that contains c.
        
    Description
    -------
        calculate the length of a given element.

    '''
    
    nbr_element = 0
    for i in c:
        nbr_element += 1
        
    return nbr_element