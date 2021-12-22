def pivot_sort(tab, pivot):
    '''

    Parameters
    ----------
    tab : list
       list of terms to sort.
    pivot : int
        it is a number which represents the pivot in order to sort tab.

    Returns
    -------
    list
        term list sort.
        
    Description
    -------
        sort a list of terms.

    '''   
    
    if len(tab) == 1 or len(tab) == 0:
        return tab
    
    elif all(x == tab[0] for x in tab):
        return tab
    
    tab_1 = []
    tab_2 = []
        
    for i in range(len(tab)):
        if tab[i] > pivot:
            tab_2.append(tab[i])
        else:
            tab_1.append(tab[i])
        
    tab_1_modif = pivot_sort(tab_1)
    tab_2_modif = pivot_sort(tab_2)
    
    return tab_1_modif + tab_2_modif