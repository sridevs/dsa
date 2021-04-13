from datastructures.node import Node


class LinearCollection:
    def __init__(self, val=None):
        self.head = self.create_node(val)
        self.tail = self.head
        self.length = 0 if val is None else 1

    @staticmethod
    def create_node(val):
        return Node(value=val)

    def peek(self):
        return self.head

    def append(self, val) -> None:
        new_node = self.create_node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.increment_length()
        if self.length == 1: self.head = self.tail

    def prepend(self, val) -> None:
        new_node = self.create_node(val)
        new_node.next = self.head
        self.head = new_node
        self.increment_length()

    def increment_length(self):
        self.length += 1

    def decrement_length(self):
        self.length -= 1
