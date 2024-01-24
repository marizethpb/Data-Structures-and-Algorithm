class Node:
    ''' Blueprint of nodes in the linked list 
    
    Attributes: 
        val (int): the value of the node
        next : memory address of the next node

    ''' 
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    ''' Blueprint of the linked list

    Attributes:
        head (node): Points to the first node in the linked list
        tail (node): Points to the last node in the linked list
        call_count (int): Counter used to measure if the method calls 
                          (except decorator) exceeded the maximum calls of 2000.

    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.call_count = 0


    def call_counter(func):
        ''' Decorator for the remaining methods. To be used for counting the occurence of function calls.
        
        Args:
            func (class method): The function to count the function calls for.
        
        '''
        def wrapper(self,*args):

            # Remind user that maximum calls is reached
            if self.call_count == 2000:
                return print("Maximum method calls reached")
            
            # Increase call_count after the function is call
            result = func(self,*args)
            self.call_count +=1

            return result
        return wrapper
    

    @call_counter
    def get(self, index: int) -> int:
        ''' Returns the value of the node if the index is valid. 
            Otherwise, negative one (-1) will be returned.
        
        Args:
            index (int): Zero-based index of the node in the linked list.
        '''
        # Return the node's val if the index is valid
        try:
            if not int(index):
                return self.head.val
            else:
                cur_node = self.head
                for _ in range(index):
                    cur_node = cur_node.next
                return cur_node.val
        
        # Return -1 if the index is invalid
        except:
            return -1
        
    @call_counter
    def addAtHead(self, val: int) -> None:
        ''' Creates and adds a head node in the linked list. 
            
            Head node will also be the tail if this is the only node in the linked list.

        Args:
            val (int): Value of the node 

        '''
        new_node = Node(val)

        # Disregard insertion if value of the node is None
        if not new_node:
            return
        
        # Insert node as head given the value of node is given
        elif self.head:
           new_node.next = self.head
           self.head = new_node

        # The first node in the linked list is both the tail and head
        else: 
            self.head = new_node
            self.tail = new_node
    

    @call_counter
    def addAtTail(self, val: int) -> None:
        ''' Creates and adds a tail node in the linked list. 
            
            Tail node will also be the head if this is the only node in the linked list.

        Args:
            val (int): Value of the node 

        '''
        new_node = Node(val)

        # Disregard insertion if value of the node is None
        if not new_node:
            return
        
        # Insert node as tail given the value of node is given
        if self.tail:
           past_node = self.tail
           past_node.next = new_node
           self.tail = new_node

        # The first node in the linked list is both the tail and head
        else: 
            self.head = new_node
            self.tail = new_node
    
    @call_counter
    def addAtIndex(self, index: int, val: int) -> None:
        ''' Creates and adds a node at a specified index in the linked list. 
            
            This node will also be the head, tail, and hand and tail if this is the first, last, 
            and only node in the linked list respecfully.

        Args:
            val (int): Value of the node 
            index (int): Zero-based index of position of the node

        '''
        try:
            new_node = Node(val)
            
            # Disregard insertion if value of the node is None
            if not new_node:
                return
            
            # Insert node as head given that the index is 0
            if index == 0:
                self.addAtHead(val)
                self.call_count -=1

            else:
                cur_node = self.head
                for i in range(1,index+1):
                    if i == index:

                        # Insert node as tail given that the index 
                        # is the size-1 of the linked list
                        if not cur_node.next:
                            self.addAtTail(val)
                            self.call_count -=1

                        # Insert node in the specified index 
                        else:
                            new_node.next = cur_node.next
                            cur_node.next = new_node
                        break
                    else:
                        cur_node = cur_node.next
        
        # Disregard insertion if the index is invalid
        except AttributeError:
            pass
            
    @call_counter
    def deleteAtIndex(self, index: int) -> None:
        ''' Deletes a node at a specified index in the linked list. 
            
            Nodes that suceeds the head or preceeds the tail will be promoted 
            as the head or tail respectfully, if the nodes to be deleted is
            the current head or tail. 

        Args:
            val (int): Value of the node 
            index (int): Zero-based index of position of the node

        '''
        # Promote suceeding node to head if head 
        # is to be removed
        if index == 0:
            prev = self.head
            self.head = self.head.next
            del prev
        
        else:
            prev_node = self.head
            cur_node = self.head.next
            for i in range(1,index+1):
                if not cur_node:
                    break
                elif i == index:

                    # Promote preceeding node to tail if tail 
                    # is to be removed
                    if not cur_node.next:
                        new_tail = prev_node
                        new_tail.next = None
                        self.tail = new_tail
                    else:
                    
                    # Unlink the node at specified index
                        prev_node.next = cur_node.next
                    break
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
