class Node:
    def __init__(self, value):
        self.next_node = None
        self.prev_node = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.record_node = None
        self.head_node = None

    def is_empty(self):
        return self.head_node is None

    def get_last_node(self):
        last_node = self.head_node

        while last_node.next_node is not None:
            last_node = last_node.next_node

        return last_node

    def get_first_node(self, carried_node):
        first_node = carried_node

        while first_node.prev_node is not None:
            first_node = first_node.prev_node

        return first_node

    def add(self, value):
        if self.head_node is None:
            self.head_node = Node(value)
        else:
            self.record_node = Node(value)
            self.head_node.prev_node = self.record_node
            self.record_node.next_node = self.head_node
            self.head_node = self.record_node

    def addAtEnd(self, value):
        last_node = self.get_last_node()

        last_node.next_node = Node(value)
        last_node.next_node.prev_node = last_node

        self.head_node = self.get_first_node(last_node)

    def print(self):
        tmp_node = self.head_node

        while tmp_node is not None:
            print(tmp_node.value)
            tmp_node = tmp_node.next_node

    def print_reverse(self):
        tmp_node = self.get_last_node()

        while tmp_node is not None:
            print(tmp_node.value)
            tmp_node = tmp_node.prev_node
