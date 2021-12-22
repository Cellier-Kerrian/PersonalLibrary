import random

options_menu = {
                1: 'Pivot = Medium',
                2: 'Pivot = Median',
                3: 'Pivot = Random',
                4: 'Pivot = Custom',
                5: 'EXIT'
               }


def menu():
    '''

    Description
    -------
         this function allows you to ask the user which pivot he wants to sort 
         the list.

    '''

    print(f"{'ID' : <8}{'Options' : <15}")
    
    for key in options_menu.keys():
        print(f"{key : <8}{options_menu[key] : <15}")
    
    flag = False
    while flag == False:
        
        option = int(input("Desired Option ID: "))
        
        if option == 1:
            flag == True
            return selection_sort(tab_definition(), 1)
        elif option == 2:
            flag == True
            return selection_sort(tab_definition(), 2)
        elif option == 3:
            flag == True
            return selection_sort(tab_definition(), 3)
        elif option == 4:
            flag == True
            return selection_sort(tab_definition(), 4)
        elif option == 5:
            return "EXIT"
        elif option > 5:
            flag == False
            print('ID non valide.')

def selection_sort(tab, n=3):
    '''

    Parameters
    ----------
    tab : list
        list of terms to sort.
    n : int, optional
        the way the pivot is chosen. The default is 3.

    Returns
    -------
    list
        term list sort.
        
    Description
    -------
       sort a tab with a sort by selection.

    '''
    
    if len(tab) == 1 or len(tab) == 0:
        return tab
    
    elif all(x == tab[0] for x in tab):
        return tab
    
    tab_1 = []
    tab_2 = []
    
    flag = False
    
    if n == 1:
        Pivot = sum(tab)/len(tab)
    elif n == 2:
        Pivot = median(tab)
    elif n == 3:
        Pivot = random.choice(tab)
    elif n == 4:
        
        print("\n")
        print(tab)
        
        while flag == False:
            Pivot = int(input("Desired pivot: "))
            
            if Pivot >= min(tab) and Pivot <= max(tab):
                flag = True
                
            else:
                print("The Pivot is not valid, it must be between the min and the max of the tab.")
                flag = False
        
    for i in range(len(tab)):
        if tab[i] > Pivot:
            tab_2.append(tab[i])
        else:
            tab_1.append(tab[i])
        
    
    tab_1_modif = selection_sort(tab_1, n)
    tab_2_modif = selection_sort(tab_2, n)
    
    return tab_1_modif + tab_2_modif
            
def tab_definition():
    '''

    Returns
    -------
    tab : liste
        term list.
        
    Description
    -------
        create a tab with values that the user provides.

    '''
    
    tab = []
    
    try:
        while True:
            print("\n\nTo stop the term implantation in the tab, press 'ENTER' or enter a term other than a number.")
            tab.append(int(input("Term(s) from the tab: ")))
            
    except:
        return tab
        
def median(tab):
    '''

    Parameters
    ----------
    tab : list
        term list.

    Returns
    -------
    int
        the median of all the terms among tab.
        
    Description
    -------
        find the median of all the terms included in a tab.

    '''
    
    medium = len(tab) // 2
    tab.sort()
    
    if not len(tab) % 2:
        return (tab[medium - 1] + tab[medium]) / 2.0
    
    return tab[medium]
        
def alea(n):
    '''

    Parameters
    ----------
    n : int
        number of terms to generate.

    Returns
    -------
    tab : list
        list of terms.
        
    Description
    -------
        create a tab of n terms between [0; 100].

    '''

    tab = []
    
    for i in range(n):
        tab.append(random.randint(0,100))
        
    return tab


# Executeur :
print(menu())