from datastructures.linear_collection import LinearCollection


class Queue(LinearCollection):

    def peek(self):
        return self.head

    def enqueue(self, val):
        self.append(val)

    def dequeue(self):
        dequeued_head, self.head = self.head, self.head.next
        self.decrement_length()
        if self.length <= 1: self.tail = self.head
        return dequeued_head
