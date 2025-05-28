"""
Linked Lists.
Benefits: Can insert a node where ever in the list for O(n)
TODO: Add type hints to class.
TODO: Add test cases.
"""


class Node:
    """
    An object for storing a single node of a linked list.
    data: data of the node.
    next_node: next node of the linked list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):  # Printing but without the print function.
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Takes O(n) time.
        :return: The number of nodes in the linked list
        """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node contianing data at the head of the list.
        Takes O(1) time.
        :param data: Data value to be added
        :return: Returns nothing.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
