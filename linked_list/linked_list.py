class LL:
    '''
    
    Description
    ------
        creation of a class LL (Linked List).
        
    '''
    def __init__(self, val, nex=None):
        '''

        Parameters
        ----------
        val : int/float/str
            the value that contains self.
        next : LL, optional
            the instance that follows self. The default is None.

        Returns
        -------
        None.
        
        Description
        -------
            create a datum of class LL (Linked List).

        '''
        self.value = val
        self.next = nex
        
    def add_before(self, other):
        '''

        Parameters
        ----------
        other : LL
            an instance of class LL.

        Returns
        -------
        None.
        
        Description
        -------
            binds two instances of class LL, adding other before self.

        '''        
        other.next = self
    
    def add_after(self, other):
        '''

        Parameters
        ----------
        other : LL
            an instance of class LL.

        Returns
        -------
        None.
        
        Description
        -------
            binds two instances of class LL, adding other after self.

        '''
        self.next = other
    
    def insert(self, other1, other2):
        '''

        Parameters
        ----------
        other1 : LL
            an instance of class LL.
        other2 : LL
            an instance of class LL.

        Returns
        -------
        None
            returns None after the insertion is done.
            
        Description
        -------
            insert an other1 between self and other2, in the string.

        '''        
        if self.next == other2:
            self.next = other1
            other1.next = other2
            return
        return self.next.insert(other1, other2)
    
    def delete(self, other):
        '''

        Parameters
        ----------
        other : LL
            an instance of class LL.

        Returns
        -------
        None
            returns None after deletion.
            
        Description
        -------
            removes an element from the string.

        '''
        if self.value == other.value:
            self.next = None
        elif self.next.value == other.value:
            self.next = self.next.next
            self.next.next = None
            other.next = None
            return 
        return self.next.delete(other)
    
    def search(self, val):
        '''

        Parameters
        ----------
        val : int/float/str
            the value that an instance of class LL may contain.

        Returns
        -------
        bool
            True = the value exists in the string.
            False = the value does not exist in the string.
            
        Description
        -------
            informs the user if the value is in the string or not.

        '''
        if self.next == None:
            return False
        elif self.value == val:
            return True
        return self.next.search(val)
        
    def __len__(self):
        '''

        Returns
        -------
        int
            returns the length of the string.
            
        Description
        -------
            returns the number of given strings.

        '''
        if self.next == None:
            return 1
        return 1 + len(self.next)
    
    def __repr__(self):
        '''

        Returns
        -------
        str
            see a representation of the string.
            
        Description
        -------
            shows the string and this data.

        '''
        if self.next == None:
            return self.value
        return str(self.value) + '--->' + str(self.next)