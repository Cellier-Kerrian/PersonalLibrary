def merge_sort(tab):
    '''

    Parameters
    ----------
    tab : list
       list of terms to sort.

    Returns
    -------
    TYPE
        list sort.
        
    Description
    -------
        sort a list of terms.

    '''
    
    len_tab = len(tab)
    
    if len_tab == 1 or len_tab == 0:
        return tab
    else:
        z = len_tab//2
        
        l1 = tab[:z]
        l2 = tab[z:]
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        
        ntab = []
        
        while l1 != [] and l2 != []:
            if l1[0] <= l2[0]:
                a = l1.pop(0)
            else:
                a = l2.pop(0)
            ntab.append(a)
        ntab = ntab + l1 + l2
        
    return ntab