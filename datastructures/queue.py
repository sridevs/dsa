from datastructures.node import Node


class Queue:
    def __init__(self, val=None):
        self.head = self.create_node(val)
        self.tail = self.head
        self.length = 0 if val is None else 1

    def peek(self):
        return self.head

    @staticmethod
    def create_node(val):
        return Node(value=val)

    def enqueue(self, val):
        new_node = self.create_node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.increment_length()
        if self.length == 1: self.head = self.tail

    def increment_length(self):
        self.length += 1

    def decrement_length(self):
        self.length -= 1

    def dequeue(self):
        dequeued_head = self.head
        self.head = self.head.next
        self.decrement_length()
        if self.length <= 1: self.tail = self.head
        return dequeued_head
