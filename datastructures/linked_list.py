from .linear_collection import LinearCollection


class LinkedList(LinearCollection):

    def get_head_value(self):
        return self.head.value

    def get_tail_value(self):
        return self.tail.value

    def insert(self, index, val):
        if index == 0: return self.prepend(val)
        if index >= self.length: return self.append(val)
        new_node = self.create_node(val)
        prev_node = self.traverse_to(index - 1)
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

    def to_list(self):
        linked_list, index, curr = [], 0, self.head
        while index < self.length:
            linked_list.append(curr.value)
            curr = curr.next
            index += 1
        return linked_list

    def delete(self, index, previous_node=None):
        if index >= self.length: index = self.length - 1
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev_node = previous_node or self.traverse_to(index - 1)
            prev_node.next = prev_node.next.next
        self.decrement_length()

    def reverse(self):
        if self.length == 0: return
        curr, nxt = self.head, self.head.next
        self.head.next, self.head, self.tail = None, self.tail, self.head
        while nxt:
            nxt.next, curr, nxt = curr, nxt, nxt.next
