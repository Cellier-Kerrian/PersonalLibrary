class FDE():
    '''
    class = FDE, creer une file a double entrer.
    '''
    def __init__(self):
        '''
        constructeur = creer une file a double entrer vide.
        return = None
        '''
        self.contenu = []
        
    def affiche(self):
        '''
        methode = Affiche la file a double entrer.
        return = list(int/str/float)
        '''
        return self.contenu
    
    def enfile_gauche(self, n):
        '''
        methode = ajoute n a la fin (a droite) de la file a double entrer.
        n = une valeur (int/str/float)
        return = 'Error!'/None
        '''
        if type(n) == list:
            return 'Error!'
        self.contenu = [n] + self.contenu
        
    def enfile_droite(self, n):
        '''
        methode = ajoute n au debut (a gauche) de la file a double entrer.
        n = une valeur (int/str/float)
        return = 'Error!'/None
        '''
        if type(n) == list:
            return 'Error!'
        self.contenu = self.contenu + [n]
        
    def defile_gauche(self):
        '''
        methode = enleve la denière valeur (celle toute a droite) de la file a double entrer.
        return = 'Error!'/une valeur (int/str/foat)
        '''
        if self.est_vide() == False:
            tmp = self.contenu[:1]
            self.contenu = self.contenu[1:]
            return tmp
        else:
            return 'Error!'
        
    def defile_droite(self):
        '''
        methode = enleve la premiere valeur (celle toute a gauche) de la file a double entrer.
        return = 'Error!'/une valeur (int/str/foat)
        '''
        if self.est_vide() == False:
            tmp = self.contenu[-1:]
            self.contenu = self.contenu[:-1]
            return tmp
        else:
            return 'Error!'
        
    def est_vide(self):
        '''
        methode = dit si la file a double entrer est vide ou non.
        return = True/False
        '''
        if len(self.contenu) != 0:
            return False
        return True
    
    def __str__(self):
        '''
        methode = permet de return une valeur si 'print(self)' est utiliser.
        return = toute les valeurs de la file a double entrer (list(int/str/float))
        '''
        return f'{self.contenu}'
    
    def __repr__(self):
        '''
        methode = permet de return une valeur si 'self' est utliser (dans le programme ou dans la console).
        return = toute les valeurs de la file a double entrer (list(int/str/float))
        '''
        return f'{self.contenu}'
    
    def __add__(self, n):
        '''
        methode = permet d'ajouter une valeur a la file a double entrer avec une siple concatenation 'self + 1'.'
        n = une valeur (int/str/float)
        return = None
        '''
        self.enfile_droite(n)
    
    def __len__(self):
        '''
        methode = permet d'obtenir la longueur de la file a double entrer.
        return = la longueur de la file a doublen entrer (int)
        '''
        ln = 0
        for i in self.contenu:
            ln += 1
        return ln
    
    def voir_droite(self):
        '''
        methode = permet d'afficher la derniere valeur (a droite) de la file a double entrer.
        return = une valeur (int/str/float)
        '''
        return self.contenu[-1:]
    
    def voir_gauche(self):
        '''
        methode = permet d'afficher la premiere valeur (a gauche) de la file a double entrer.
        return = une valeur (int/str/float)
        '''
        return self.contenu[:1]

def inverse(F):
    '''
    fonction = permet de renvoyer une nouvelle liste qui comporte les terme d'une file a double entrer mais avec les valeur dans le sens inverse.
    F = une file a double entrer
    return =  une liste comportant toute les valeur de la file a double entrer mais dans le sens inverse (list(int/str/float))
    '''
    tmp = []
    for i in range(len(F)):
        tmp.append(F.defile_droite()[0])
    for i in tmp:
        F.enfile_gauche(i)
    return tmp

###############################################################################
###############################################################################
# Partie 1:
    
# 1
# • creer() -> []
# • enfiler_a_droite("a") -> ["a"]
# • enfiler_a_gauche("b") -> ["b", "a"]
# • defile_a_droite() -> ["b"]
# • enfile_a_gauche("c") -> ["c", "b"]
# • deficle_a_gauche() -> ["b"]
# • enfile_a_droite("d") -> ["b", "d"]
# • defile_a_gauche() -> ["d"]
# • enfile_a_gauche("e") -> ["d", "e"]
# • enfile_a_gauche("f") -> ["d", "e", "f"]
# • defile_a_gauche() -> ["e", "f"]

# 2
def concatene(F1, F2):
    '''
    fonction = permet de concatener deux file a double entrer.
    F1 = Premiere file a double entrer
    F2 = deuxieme file a double entrer
    return = une liste comportant toute les valeur des deux file a double entrer (list(int/str/float))
    '''
    F_tmp = FDE()
    for i in F1.affiche():
        F_tmp.enfile_gauche(i)
    for i in F2.affiche():
        F_tmp.enfile_gauche(i)
    return F_tmp