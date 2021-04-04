from .linked_list import LinkedList
from .two_way_node import TwoWayNode


class DoublyLinkedList(LinkedList):

    @staticmethod
    def create_node(val):
        return TwoWayNode(value=val)

    def append(self, val) -> None:
        prev_node = self.tail
        super().append(val)
        self.tail.prev = prev_node

    def prepend(self, val) -> None:
        pointing_head = self.head
        super().prepend(val)
        pointing_head.prev = self.head

    def insert(self, index, val):
        prev_node = self.traverse_to(index-1)
        super().insert(index, val)
        inserted_node = prev_node.next
        inserted_node.prev = prev_node
        inserted_node.next.prev = inserted_node

    def delete(self, index, previous_node=None):
        if index == 0:
            self.head.next.prev = None
        else:
            previous_node = self.traverse_to(index-1)
            if index != self.length-1:
                next_node = previous_node.next.next
                next_node.prev = previous_node
        super().delete(index, previous_node)
