class Stack:
    '''
    
    Description
    ------
        creation of a class Stack.
        
    '''
    
    def __init__(self):
        '''
        
        Description
        -------
            constructor: create the content of the self value of the Stack class.

        '''
        self.contents = []
    
    def empty(self):
        '''
            
        Returns
        -------
        bool
            True : is empty.
            False : is not empty.
            
        Description
        -------
            informs whether self is empty or not.

        '''
        return self.contents == []
    
    def stacked(self, n):
        '''

        Parameters
        ----------
        n : stack
            an attribute of the class stack.
            
        Returns
        -------
        None.

        Description
        -------
            stack an attribute of the class stack.

        '''
        self.contents.append(n)
        
    def unstacked(self):
        '''

        Returns
        -------
        first : int/float/str/bool
            displays the first term in the list before moving the stack.

        Description
        -------
            unstacked the last element of the stack.

        '''
        if self.empty() == True:
            return None
        else:
            first = self.contents[-1]
            del self.contents[-1]
            return first
    
    
    def attach(self):
        '''

        Returns
        -------
        list
            displays all the values of contained in the stack starting from 
            self.

        Description
        -------
            displays all the values of contained in the stack starting from 
            self.

        '''
        return self.contents

    def __len__(self):
        '''

        Returns
        -------
        n : int
            displays the stack length.
        
        Description
        -------
            displays the stack length.

        '''
        stack_b = Stack()
        n = 0
        while not self.empty():
            n += 1
            stack_b.unstacked(self.stacked())
        while not stack_b.empty():
            self.unstacked(stack_b.stacked())
        return n

    def __repr__(self):
        '''

        Returns
        -------
        str
            displays self.
            
        Description
        -------
            displays self.

        '''
        return self.contents
      
      
class Queue:
    def __init__(self):
        '''

        Description
        -------
            creation of a class queue.

        '''
        self.contents = []
    
    def empty(self):
        '''
        
        Description
        -------
            informs whether self is empty or not.
            
        Returns
        -------
        bool
            True : is empty.
            False : is not empty.

        '''
        return self.contents == []
    
    def put(self, n):
        '''

        Parameters
        ----------
        n : Queue
            an attribute of the class queue.
            
        Returns
        -------
        None.

        Description
        -------
            threads an attribute from the class queue at the end.

        '''
        self.contents.append(n)
        
    def scroll(self):
        '''

        Returns
        -------
        first : Queue
            displays the first term in the list before scrolling through the 
            queue.

        Description
        -------
            scrolls the last element of the queue.

        '''
        if self.empty() == True:
            return None
        else:
            first = self.contents[0]
            del self.contents[0]
            return first
        
    def attach(self):
        '''

        Returns
        -------
        list
            displays all the values of contained in the queue starting from 
            self.

        Description
        -------
            displays all the values of contained in the queue starting from 
            self.

        '''
        return self.contents

    def __len__(self):
        '''

        Returns
        -------
        n : int
            displays the length of the queue.
        
        Description
        -------
            displays the length of the queue.

        '''
        queue_b = Queue()
        n = 0
        while not self.empty():
            n += 1
            queue_b.put(self.scroll())
        while not queue_b.empty():
            self.put(queue_b.scroll())
        return n

    def __repr__(self):
        '''

        Returns
        -------
        str
            displays self.
            
        Description
        -------
            displays self.

        '''
        return f"Queue(->{self.file}->)"

##############################################################################

class Stack2:
    def __init__(self):
        '''

        Description
        -------
            creation of a class stack with two queue.

        '''
        self.stack1 = Stack()
        self.stack2 = Stack()

    def exchange(self, stack):
        '''

        Parameters
        ----------
        stack : Satck
            an element of the class queue.

        Returns
        -------
        None.
        
        Description
        -------
            exchange an element given in parameter which is in a File to go adns another File.

        '''
        if stack:
            length = len(self.stack1)
            for i in range(length):
                self.stack2.stacked(self.stack1.unstacked())
        else:
            length = len(self.stack2)
            for k in range(length):
                self.stack1.stacked(self.stack2.unstacked())

    def put(self, val=0):
        '''

        Parameters
        ----------
        val : int, optional
            a value. The default is 0.

        Returns
        -------
        None.
        
        Description
        -------
            add a value to the stack.

        '''
        self.stack1.stacked(val)

    def scroll(self):
        '''

        Returns
        -------
        first : Queue
            displays the first term in the list before scrolling through the 
            queue.

        Description
        -------
            scrolls the last element of the queue.

        '''
        if self.stack1.empty():
            return None
        else:
            self.exchange(1)
            return_value = self.stack2.unstacked()
            self.exchange(0)
            return return_value

    def empty(self):
        '''
            
        Returns
        -------
        bool
            True : is empty.
            False : is not empty.
            
        Description
        -------
            informs whether self is empty or not.

        '''
        return self.stack1.empty()

    def __len__(self):
        '''

        Returns
        -------
        n : int
            displays the stack length.
        
        Description
        -------
            displays the stack length.

        '''
        return len(self.stack1)

    def __repr__(self):
        '''

        Returns
        -------
        str
            displays self.
            
        Description
        -------
            displays self.

        '''
        self.exchange(1)
        return_value = self.stack2.stack.copy()
        self.exchange(0)
        return f"Stack(->{return_value}->)"

class Queue2:
    def __init__(self):
        '''

        Description
        -------
            creation of a class queue with two Stack.

        '''
        self.queue1 = Queue()
        self.queue2 = Queue()

    def empty(self):
        '''
            
        Returns
        -------
        bool
            True : is empty.
            False : is not empty.
            
        Description
        -------
            informs whether self is empty or not.

        '''
        return self.queue1.empty()

    def stacked(self, data=0):
        '''

        Parameters
        ----------
        n : stack
            an attribute of the class queue.
            
        Returns
        -------
        None.

        Description
        -------
            stack an attribute of the class queue.

        '''
        self.queue2.put(data)
        for _ in range(len(self.queue1)):
            self.queue2.put(self.queue1.scroll())
        for _ in range(len(self.queue2)):
            self.queue1.put(self.queue2.scroll())

    def unstacked(self):
        '''

        Returns
        -------
        first : int/float/str/bool or None
            None = if stack is empty.
            else = displays the first term in the list before moving the stack.

        Description
        -------
            unstacked the last element of the queue.

        '''
        if self.empty():
            return None
        else:
            return self.queue1.scroll()

    def __len__(self):
        '''

        Returns
        -------
        n : int
            displays the length of the queue.
        
        Description
        -------
            displays the length of the queue.

        '''
        return len(self.queue1)

    def __repr__(self):
        '''

        Returns
        -------
        str
            displays self.
            
        Description
        -------
            displays self.

        '''
        return f"Queue1 : {self.queue1} \nQueue2 : {self.queue2}"