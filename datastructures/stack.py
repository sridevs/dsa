from datastructures.node import Node


class Stack:
    def __init__(self, val):
        self.head = self.create_node(val)
        self.tail = self.head
        self.length = 1

    def peek(self):
        return self.head

    def push(self, val):
        new_node = self.create_node(val)
        new_node.next = self.head
        self.head = new_node
        self.increment_length()

    def increment_length(self):
        self.length += 1

    def decrement_length(self):
        self.length -= 1

    @staticmethod
    def create_node(val):
        return Node(value=val)

    def pop(self):
        self.head, popped_head = self.head.next, self.head
        self.decrement_length()
        if self.length <= 1: self.tail = self.head
        return popped_head
