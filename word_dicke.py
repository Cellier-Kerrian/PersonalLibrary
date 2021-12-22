def dycke(X, Y, n):
    '''
    
    Parameters
    ----------
    X : str
        it is the value X which must be in n.
    Y : str
        it is the value Y which must be in n.
    n : str
        this is the word to be tested.

    Returns
    -------
    bool
        True : n is a dycke word.
        False : n is not a dycke word.
        
    Descrition
    -------
        This function allows you to tell if a character string is a dycke word.

    '''
    
    number = 0
    for i in str(n):
        if i == str(X):
            number += 1
        elif i == str(Y):
            number -= 1
        else:
            return False
        
        if number < 0:
            return False
    
    return number == 0


# Exemple :
print(dycke('A', 'B', 'AABB')) # return True
print(dycke('A', 'B', 'ABB')) # return False