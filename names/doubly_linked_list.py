#
# Define data structures
#

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
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
        nodes = []
        node = self.head
        for i in range(self.length):
            nodes.append(str(node.value))
            node = node.next
        return f"[{','.join(nodes)}]"
  
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.length == 0:
            node = ListNode(value, None, None)
            self.head = node
            self.tail = node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

        self.length += 1
  
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        removed_head = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1

        return removed_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length == 0:
            node = ListNode(value, None, None)
            self.head = node
            self.tail = node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        removed_tail = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev

        self.length -= 1

        return removed_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        node.delete()
        self.length -= 1
    
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value
        node = self.head

        for i in range(self.length):
            if node.value > max_value:
                max_value = node.value
            node = node.next

        return max_value
