#
# Dependencies
#

from doubly_linked_list import DoublyLinkedList

#
# Define data structure
#

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
    
    def pop(self):
        if self.len() == 0:
            return None

        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
