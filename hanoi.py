def hanoi(n, origin, passage, destination):
    '''

    Parameters
    ----------
    n : int
        number of disc on the original tower.
    origin : str
        the name of the original tower.
    passage : str
        the name of the intermediate tower.
    destination : str
        the name of the tower where all the discs will be found at the end.

    Returns
    -------
    None.
    
    Description
    -------
        displays the path to follow to move all disks from the original tower 
        to the destination tower.

    '''
    
    if n ==  0:
        pass
    else:
        hanoi(n-1, origin, destination, passage)
        print(origin + " → " + destination)
        hanoi(n-1, passage, origin, destination)
    
    
# Exemple :
hanoi(10, "A", "B", "C")