from dlinkedlist import LinkedList

class Queue:
    def __init__(self):
        self.inner_list = LinkedList()

    def is_empty(self):
        return self.inner_list.is_empty()

    def insert(self, value):
        if self.is_empty():
            self.inner_list.add(value)
            return

        self.inner_list.addAtEnd(value)

    def remove(self):
        if self.is_empty():
            print("No elements in Queue")
            return None

        last_node = self.inner_list.get_last_node()
        node_value = last_node.value

        prev_node = last_node.prev_node
        prev_node.next_node = None

        self.inner_list.head_node = self.inner_list.get_first_node(prev_node)

        return node_value

    def print(self):
        if self.is_empty():
            print("No elements in Queue")
            return

        self.inner_list.print_reverse()

queue = Queue()

queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)

queue.print()

queue.remove()

queue.print()
