def insertion_sort(tab):
    '''

    Parameters
    ----------
    tab : TYPE
        list of terms to sort. The default is None.

    Returns
    -------
    tab : TYPE
       term list sort.
    
    Description
    -------
        sort a list of terms.

    '''
    
    for i in range(1,len(tab)):
        key = tab[i]
        j = i-1
        
        while j>=0 and tab[j] > key:
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = key
        
    return tab