def prime_factors(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    list
        prime factor list.
        
    Description
    -------
        review a list with the prime factor(s) of n.

    '''
    
    if n==1:
        return []
    else :
        for i in range(2,n+1):
            if n%i==0:
                return [i] + prime_factors(n//i)