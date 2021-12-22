def decimal_hexadecimal(n):
    '''

    Parameters
    ----------
    n : int
        nombre décimal.

    Returns
    -------
    str
        hexadecimal number.
        
    Description
    -------
        returns a decimal number in hexadecimal.

    '''
    
    if n < 0 :
        return "¡ERROR! \"n\" inferior than 0."
    elif n == 0:
        return "0"
    elif n == 1:
        return "1"
    elif n == 2:
        return "2"
    elif n == 3:
        return "3"
    elif n == 4:
        return "4"
    elif n == 5:
        return "5"
    elif n == 6:
        return "6"
    elif n == 7:
        return "7"
    elif n == 8:
        return "8"
    elif n == 9:
        return "9"
    elif n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"
    
    else:
        nombre_hexa = ""
        return nombre_hexa + decimal_hexadecimal(n // 16) + decimal_hexadecimal(n % 16)