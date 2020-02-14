"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"\n data: {self.value} \n prev: {self.prev} \n next: {self.next}"
        #adding a repr here and a str below helps to see an actual representation of the list if you want to print it out. 


    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(self, value, current_next)
        if current_next:
            current_next.prev = self.next


    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(self, value, current_prev)
        if current_prev:
            current_prev.next = self.prev


    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"{self.head}"


    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value): # would rethink using insert_before as it doesn't always reassign pointers properly for head and tail
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head

        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self): #this one is ok although I think you can just use delete method
        cur_node = self.head
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = self.head.prev
                self.head = self.head.next

            self.length -= 1
            return cur_node.value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value): #rethink using the built in insert_after method on this one

        if not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            

        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self): #this one is ok
        cur_node = self.tail
        if self.tail:
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                self.tail.prev.next = self.tail.next
                self.tail = self.tail.prev

            self.length -= 1
            return cur_node.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node != self.head:
            self.delete(node) #double check that this method takes parameters
            self.add_to_head(node.value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node != self.tail:
            self.delete(node) #couple of different edge cases that need to be checked here. 
            self.add_to_tail(node.value)
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node): #this works
        if not self.head and not self.tail:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node.prev is None:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        node.delete() #you used this method correctly here.

        self.length -= 1 

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        cur_node = self.head
        cur_max = cur_node.value

        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.value > cur_max:
                cur_max = cur_node.value #missing your iterator here to keep the loop going...

        return cur_max