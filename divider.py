def divider(n):
    '''

    Parameters
    ----------
    n : int
        decimal number.

    Returns
    -------
    None.
    
    Description
    -------
        displays all divisors from 0 to n.

    '''
    
    for i in range(1,n +1):
      if n % i == 0 :
        print(i)