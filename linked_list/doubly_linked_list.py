class DLL:
    '''
    
    Description
    ------
        creation of a class DLL (Doubly Linked List).
        
    '''
    def __init__(self, val, nex=None, pre=None):
        '''

        Parameters
        ----------
        val : int/float/str
            the value that contains self.
        next : DLL, optional
            the instance that follows self. The default is None.
        pre : DLL, optional
            the instance that precedes self. The default is None.

        Returns
        -------
        None.
        
        Description
        -------
            create a datum of class DLL (Doubly Linked List).

        '''
        self.value = val
        self.next = nex
        self.previous = pre
        
    def add_before(self, other):
        '''

        Parameters
        ----------
        other : DLL
            an instance of class DLL.

        Returns
        -------
        None.
        
        Description
        -------
            binds two instances of class DLL, adding other before self.

        '''       
        self.previous = other
        other.next = self
    
    def add_after(self, other):
        '''

        Parameters
        ----------
        other : DLL
            an instance of class DLL.

        Returns
        -------
        None.
        
        Description
        -------
            binds two instances of class DLL, adding other after self.

        '''
        self.next = other
        other.previous = self
    
    def insert(self, other1, other2):
        '''

        Parameters
        ----------
        other1 : DLL
            an instance of class DLL.
        other2 : DLL
            an instance of class DLL.

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
            other1.previous = self
            other1.next = other2
            other2.previous = other1
            return
        return self.next.insert(other1, other2)
    
    def delete(self, other):
        '''

        Parameters
        ----------
        other : DLL
            an instance of class DLL.

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
            other.previous = None
        elif self.next.value == other.value:
            self.next = self.next.next
            self.next.previous = self.next
            self.next.next = None
            self.next.previous = None
            return
        return self.next.delete(other)
        
    def left_search(self, val):
        '''

        Parameters
        ----------
        val : int/float/str
            the value that an instance of class DLL may contain.

        Returns
        -------
        bool
            True = the value exists in the string.
            False = the value does not exist in the string.
            
        Description
        -------
            informs the user if the value is in the string or not (search by the left).

        '''
        if self.previous == None:
            return False
        elif self.value == val:
            return True
        return self.previous.left_search(val)
       
    def right_search(self, val):
        '''

        Parameters
        ----------
        val : int/float/str
            the value that an instance of class DLL may contain.

        Returns
        -------
        bool
            True = the value exists in the string.
            False = the value does not exist in the string.
            
        Description
        -------
            informs the user if the value is in the string or not (search by the right).

        '''
        if self.next == None:
            return False
        elif self.value == val:
            return True
        return self.next.right_search(val)
       
    def display_left(self):
        '''

        Returns
        -------
        str
            see a representation of the string from the left.
            
        Description
        -------
            shows the string and this data to the left.

        '''
        if self.previous == None:
            return self.value
        return self.previous.display_left() + '<---' + str(self.value)
         
    def display_right(self):
        '''

        Returns
        -------
        str
            see a representation of the string from the right.
            
        Description
        -------
            shows the string and this data to the right.

        '''
        if self.next == None:
            return self.value
        return str(self.value) + '--->' + self.next.display_right()
   
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