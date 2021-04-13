from datastructures.linear_collection import LinearCollection


class Stack(LinearCollection):

    def push(self, val):
        self.prepend(val)

    def pop(self):
        self.head, popped_head = self.head.next, self.head
        self.decrement_length()
        if self.length <= 1: self.tail = self.head
        return popped_head
