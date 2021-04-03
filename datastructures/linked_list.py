from node import Node


class LinkedList:
    def __init__(self, val):
        self.head = Node(value=val)
        self.tail = self.head
        self.length = 1

    def get_head_value(self):
        return self.head.value

    def get_tail_value(self):
        return self.tail.value

    def append(self, val) -> None:
        new_node = Node(value=val)
        self.tail.next = new_node
        self.tail = new_node
        self.increment_length()

    def prepend(self, val) -> None:
        new_node = Node(value=val)
        new_node.next = self.head
        self.head = new_node
        self.increment_length()

    def insert(self, index, val):
        if index == 0: return self.prepend(val)
        if index >= self.length: return self.append(val)
        new_node = Node(value=val)
        prev_node = self.traverse_to(index-1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.increment_length()

    def traverse_to(self, target_index):
        if target_index >= self.length: return self.tail
        curr_index, curr_node = 0, self.head
        while curr_index < target_index:
            curr_node = curr_node.next
            curr_index += 1
        return curr_node

    def increment_length(self):
        self.length += 1

    def decrement_length(self):
        self.length -= 1

    def get_list(self):
        linked_list, index, curr = [], 0, self.head
        while index < self.length:
            linked_list.append(curr.value)
            curr = curr.next
            index += 1
        return linked_list

    def delete(self, index):
        pointing_node = self.traverse_to(index-1)
        pointing_node.next = pointing_node.next.next
        self.decrement_length()
