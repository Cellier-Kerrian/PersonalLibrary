def dichotomy_search(tab, x, low=None, high=None):
    '''

    Parameters
    ----------
    tab : list
        list of terms sort.
    x : int
        value to look for in tab.
    low : TYPE, optional
        the part of tab where you have to start looking.
    high : TYPE, optional
        the part of tab where you have to finish searching. The default is None.

    Returns
    -------
    str/int
        if str : displays an error.
        if int : index of the value in tab.
        
    Description
    -------
        displays the index where x is in tab, tab being a sort list 
        (no duplicates).

    '''
    
    if low == None:
        low = 0
    if high == None:
        high = len(tab)-1
 
    
    if high >= low:
        mid = (high + low) // 2
 
        
        if tab[mid] == x:
            return mid
 
        elif tab[mid] > x:
            return dichotomy_search(tab, x, low, mid - 1 )
 
        else:
            return dichotomy_search(tab, x, mid + 1, high)
 
    else:
        return "This element is not present in your tab."


# Exemple :
print(dichotomy_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)) # return 2
print(dichotomy_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # return "This ..."