#
# Dependencies
#

from doubly_linked_list import DoublyLinkedList

#
# Define data structure
#

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)
    
    def dequeue(self):
        if self.len() == 0:
            return None

        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
