def prime_number(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    bool
        True : it is a prime number.
        False : it is not a prime number.

    '''
    
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
    
def all_prime_number(n):
    '''

    Parameters
    ----------
    n : TYPE
        decimal number.

    Returns
    -------
    liste_p : list
        prime number list.
        
    Description
    -------
        displays a list including all the first ones between 1 and n.

    '''
    
    liste_p = []
    for o in range(2, n+1):
        liste = []
        for i in range(2,o):
            if o % i == 0 :
                liste = liste + [i]
        if liste == []:
            liste_p = liste_p + [o]
    return liste_p