import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False

        if target > self.value:
            if self.right:
                if self.right.contains(target):
                    return True
        elif target < self.value:
            if self.left:
                if self.left.contains(target):
                    return True
        elif target == self.value:
            return True
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self:
            cur_max = self
            while cur_max.right is not None:
                cur_max = cur_max.right
            return cur_max.value
        else:
            return None

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        cur_node = queue.storage.head

        while cur_node is not None:
            if cur_node.value.left:
                queue.enqueue(cur_node.value.left)
            if cur_node.value.right:
                queue.enqueue(cur_node.value.right)
            cur_node = cur_node.next

        while queue.size > 0:
            dequeued_node = queue.dequeue()
            print(dequeued_node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
