from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.inner_list = LinkedList()

    def is_empty(self):
        return self.inner_list.is_empty()

    def push(self, value):
        self.inner_list.add(value)

    def pop(self):
        if self.is_empty():
            return None

        node_value = self.inner_list.head_node.value

        self.inner_list.head_node = self.inner_list.head_node.next_node

        return node_value

    def print(self):
        if not self.is_empty():
            self.inner_list.print()
        else:
            print("stack empty")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print()

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.print()
