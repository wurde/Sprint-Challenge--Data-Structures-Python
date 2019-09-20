#
# Dependencies
#

import math
from dll_queue import Queue
from dll_stack import Stack

#
# Define data structure
#

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()
        self.lastPrintedValue = -math.inf

    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
            return

        focusNode = self
        while True:
            if value == focusNode.value:
                return

            if value < focusNode.value:
                if focusNode.left is None:
                    focusNode.left = BinarySearchTree(value)
                    return
                else:
                    focusNode = focusNode.left

            if value > focusNode.value:
                if focusNode.right is None:
                    focusNode.right = BinarySearchTree(value)
                    return
                else:
                    focusNode = focusNode.right

    def contains(self, target):
        focusNode = self

        while focusNode is not None:
            if target == focusNode.value:
                return True
            elif target < focusNode.value:
                focusNode = focusNode.left
            else:
                focusNode = focusNode.right
        
        return False

    def get_max(self):
        focusNode = self

        while True:
            maxValue = focusNode.value

            if focusNode.right is None:
                return maxValue
            else:
                focusNode = focusNode.right

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(node.value)

        if node.left:
            self.queue.enqueue(node.left)
        if node.right:
            self.queue.enqueue(node.right)

        while self.queue.len() > 0:
            self.bft_print(self.queue.dequeue())

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)

        if node.left:
            self.stack.push(node.left)
        if node.right:
            self.stack.push(node.right)

        while self.stack.len() > 0:
            self.dft_print(self.stack.pop())

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)

        print(node.value)
