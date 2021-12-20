class Arbre:
    '''
    class = Arbre, creer un arbre.
    '''
    def __init__(self, val="None"):
        '''
        constructeur = creer un noeud/une feuille d'un arbre.
        val = valeur (defaut="None") str
        '''
        self.valeur = val
        self.enfant = []
        
    def ajouter(self, enfant):
        '''
        methode = ajouter, permet d'ajouter une feuille sous un Noeux.
        enfant = Arbre (noeud/feuille de la class Arbre)
        return = None
        '''
        self.enfant.append(enfant)
        
    def supprime(self, other, del_all=True):
        '''
        methode = supprime, permet de supprimer tout ou un enfant d'un noeud (le choix est possible grace a la variable del_all).
        other = Arbre (noeud/feuille de la class Arbre)
        del_all = True/False (defaut = True)
        return = None
        '''
        if del_all == True and other in self.enfant:
            self.enfant = []
        elif del_all == False and other in self.enfant:
            self.enfant.remove(other)
            self.enfant.append(other.enfant)
        
    def est_feuille(self):
        '''
        methode = est_feuille, permet de savoir si self est un noeud ou un feuille dans un arbre.
        return = True/False
        '''
        return self.enfant == []
    
    def taille(self):
        '''
        methode = taille, permet d'avoir la taille d'un arbre de racine self.
        return = (int)
        '''
        if self.feuille():
            return 0
        else:
            for i in self.enfant:
                return 1 + i.taille()
        
    def hauteur(self):
        '''
        methode = hauteur, permet d'avoir la hauteur d'un arbre de racine self.
        return = 
        '''
        if self.feuille():
            return -1
        else:
            for i in self.enfant:
                return 1 + i.hauteur()
    
    def profondeur(self):
        '''
        methode = profondeur, permet d'avoir la profondeur d'un arbre de racine self.
        return = 
        '''
        pass
    
    def degre(self):
        '''
        methode = degre, permet d'avoir le degret d'un arbre de racine self.
        return = 
        '''
        pass
            
    def afficher(self, n=0):
        '''
        methode = afficher, permet d'afficher un arbre de racine self.
        return = (str)
        '''
        print(n*'-'+self.valeur)
        for i in self.enfant:
            i.afficher(n+1)
            
    def modifie_donnee(self, val):
        '''
        methode = modifie_donnee, permet de modifier la veleur de self dans un arbre.
        val = valeur (int/float/str)
        return = None
        '''
        self.valeur = val
    
    def get(self):
        '''
        methode = get, permet de return les fils de self.
        return = Arbre (instance de la class Arbre)
        '''
        return self.enfant
    
    def __repr__(self):
        '''
        methode = __repr__, permet d'afficher ce que contien self.
        return = (int/float/str)
        '''
        return self.valeur
    
###############################################################################
###############################################################################

class Arbre_binaire:
    '''
    class = Arbre_binaire, creer un arbre binaire.
    '''
    def __init__(self, val):
        '''
        constructeur = creer un noeud/une feuille d'un arbre binaire.
        val = valeur (int/float)
        '''
        if type(val) == int or type(val) == float:
            self.valeur = val
            self.enfant_g = None
            self.enfant_d = None
        else:
            pass
        
    
    def ajouter(self, g=None, d=None):
        '''
        methode = ajouter, permet d'ajouter une feuille sous un Noeux.
        g = Arbre (defaut = None) (noeud/feuille de la class Arbre)
        d = Arbre (defaut = None) (noeud/feuille de la class Arbre)
        return = None
        '''
        if g != None:
            self.enfant_g = g
        if d != None:
            self.enfant_d = d
            
    def supprimer(self, other, del_all=True):
        '''
        methode = supprime, permet de supprimer tout ou un enfant d'un noeud (le choix est possible grace a la variable del_all).
        other = Arbre (noeud/feuille de la class Arbre)
        del_all = True/False (defaut = True)
        return = None
        '''
        if (del_all == True) and (other in self.enfant):
            self.enfant = []
        elif (del_all == False) and (other in self.enfant):
            self.enfant.remove(other)
            self.enfant.append(other.enfant)
        
    def est_feuille(self):
        '''
        methode = feuille, permet de savoir si self est un noeud ou un feuille dans un arbre binaire.
        return = True/False
        '''
        return self.enfant_g == None and self.enfant_d == None
    
    def taille(self):
        '''
        methode = taille, permet d'avoir la taille d'un arbre de racine self.
        return = (int)
        '''
        if self.feuille():
            return 0
        else:
            return 1 + self.enfant_g.taille() + self.enfant_d.taille()
    
    def hauteur(self):
        '''
        methode = hauteur, permet d'avoir la hauteur d'un arbre de racine self.
        return = 
        '''
        if self.feuille():
            return 0
        else:
            return 1 + max(self.enfant_d.hauteur(), self.enfant_g.hauteur())
    
    def profondeur(self):
        '''
        methode = profondeur, permet d'avoir la profondeur d'un arbre de racine self.
        return = 
        '''
        # if self.feuille():
        #     return 0
        # else:
        #     for i in [self.enfant_g, self.enfant_d]:
        #         return 1 + i.profondeur()
    
    def degre(self):
        '''
        methode = degre, permet d'avoir le degret d'un arbre de racine self.
        return = 
        '''
        pass

    def afficher(self, n=0):
        '''
        methode = afficher, permet d'afficher un arbre de racine self.
        return = (str)
        '''
        total = n*"-" + str(self.valeur)
        for j in [self.enfant_g, self.enfant_d]:
            if j != None:
                total += "\n" + j.afficher(n+1)
        return total
    
    def modifie_donnee(self, val):
        '''
        methode = modifie_donnee, permet de modifier la veleur de self dans un arbre.
        val = valeur (int/float/str)
        return = None
        '''
        self.valeur = val
    
    def est_binaire_tri(self):
        '''
        methode = est_binaire_tri, permet d.
        return = 
        '''
        pass
    
    def get_gauche(self):
        '''
        methode = get_gauche, permet de return le fil gauche de self.
        return = Arbre_binaire (instance de la class Arbre_binaire)
        '''
        return self.enfant_g
    
    def get_droite(self):
        '''
        methode = get_droite, permet de return le fil droite de self.
        return = Arbre_binaire (instance de la class Arbre_binaire)
        '''
        return self.enfant_d
    
    def __lt__(self, other):
        '''
        methode = __lt__, permet d.
        other = autre instance de la class Arbre_binaire
        return = True/False
        '''
        return (self.valeur < other.valeur or self.valeur == other.valeur)
        
    def __gt__(self, other):
        '''
        methode = __qt__, permet de comparer deux instances de la class Arbre_binaire (>).
        other = autre instance de la class Arbre_binaire
        return = True/False
        '''
        return (self.valeur > other.valeur or self.valeur == other.valeur)
        
    def __add__(self, other):
        '''
        methode = __add__, permet d'additionner deux instances de la class Arbre_binaire.
        return = True/False
        '''
        return self.valeur + other.valeur
        
    def __repr__(self):
        '''
        methode = __repr__, permet d'afficher ce que contient self.
        return = (int/float/str)
        '''
        return f"({self.valeur}, ({self.enfant_g}, {self.enfant_d})"
