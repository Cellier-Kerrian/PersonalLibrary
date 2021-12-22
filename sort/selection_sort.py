import random

def selection_sort(nbr=10, tab=None):
    '''

    Parameters
    ----------
    nbr : int
        number of values in tab, tab being created randomly. The default is 10.
    tab : list
        list of terms to sort. The default is None.

    Returns
    -------
    tab : list
        term list sort.
        
    Description
    -------
        sort a list of terms.

    '''
    
    if type(nbr) == list:
        tab = nbr
    
    if tab is None:
        tab = randomly(nbr)

    N = len(tab)
    for i in range(0, N-1):
        pos = search_min_position(tab, i)
        swap_items(tab, i, pos)
    return tab
    
def search_min_position(tab, i):
    '''

    Parameters
    ----------
    tab : list
        term list.
    i : int
        number that represents an index of tab.

    Returns
    -------
    index_min : int
        the minimum index of tab.
        
    Description
    -------
        returns the index of the smallest value among tab.

    '''
    
    valeur_min = tab[i]
    index_min = i
    for j in range(i, len(tab)):
        if tab[j] < valeur_min:
            index_min = j
            valeur_min = tab[j]
    return index_min

def swap_items(tab, i, pos):
    '''

    Parameters
    ----------
    tab : list
        term list.
    i : int
        number that represents an index of tab.
    pos : int
        number that represents an index of tab.

    Returns
    -------
    None.
    
    Description
    -------
        change the peas element in place of the i element.
    
    '''
    
    temp = tab[i]
    tab[i] = tab[pos]
    tab[pos] = temp

def randomly(nbr):
    '''

    Parameters
    ----------
    nbr : int
        number which represents the number of elements that will contain the 
        list which is returned.

    Returns
    -------
    tab : list
        list of number element(s).
        
    Description
    -------
        create a list of number of element(s), each one chooses randomly 
        between 0 and 100.

    '''
    
    tab = []
    for i in range(nbr):
        tab.append(random.randrange(0,100))
    return tab