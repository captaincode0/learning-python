class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.record_node = None

    def add(self, value):
        if self.head_node == None:
            self.head_node = Node(value)
        else:
            self.record_node = Node(value)
            self.record_node.next_node = self.head_node
            self.head_node = self.record_node

    def is_empty(self):
        return self.head_node is None

    def print(self):
        tmp_node = self.head_node

        while tmp_node is not None:
            print(tmp_node.value)
            tmp_node = tmp_node.next_node
