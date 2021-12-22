import csv


def csv_vers_table(fichier, separateur = ',', encodage = 'utf8'):
	'''

    Parameters
    ----------
    fichier : str
        path to csv file.
    separateur : str, optional
        the separator between each data of the csv file. The default is ','.
    encodage : TYPE, optional
        csv file encoding type. The default is 'utf8'.

    Returns
    -------
    table : dict
        a dictionary containing the values of the csv file.
    
    Description
    -------
        creation of a dictionary containing the values of the csv file.

    '''
    
	with open(fichier, 'r', encoding = encodage) as f :
		lecteur = csv.DictReader(f, delimiter = separateur)
		table = [dict(ligne) for ligne in lecteur]
	return table

def table_vers_csv(table, fichier, encodage = 'utf8'):
    '''

    Parameters
    ----------
    table : dict
        dictionary.
    fichier : str
        name of the file at creation.
    encodage : str, optional
        encoding type of the file. The default is 'utf8'.

    Returns
    -------
        None.
    
    Description
    -------
        creation of a csv file from a dictionary.

    '''
    
    with open(fichier, 'w', encoding = encodage, newline='') as f:
        objet = csv.DictWriter(f, list(table[0].keys()))
        objet.writeheader()
        for ligne in table:
            objet.writerow(ligne)