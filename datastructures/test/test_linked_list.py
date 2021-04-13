import unittest

from ..linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList(3)

class TestInit(TestLinkedList):
    def test_initial_head_value(self):
        self.assertEqual(3, self.linked_list.get_head_value())

    def test_initial_tail_value(self):
        self.assertEqual(3, self.linked_list.get_tail_value())

    def test_length(self):
        self.assertEqual(1, self.linked_list.length)

    def test_creation_of_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, linked_list.tail, None)
        self.assertEqual(linked_list.length, 0)


class TestOperations(TestLinkedList):
    def test_append_on_empty_list(self):
        empty_list = LinkedList()
        empty_list.append(3)
        self.assertEqual(3, empty_list.get_head_value(), empty_list.get_tail_value())

    def test_append(self):
        self.linked_list.append(5)
        self.assertEqual(5, self.linked_list.get_tail_value())
        self.assertEqual(self.linked_list.head.next.value, self.linked_list.get_tail_value())
        self.assertEqual(2, self.linked_list.length)
        self.linked_list.append(4)
        self.assertEqual(5, self.linked_list.head.next.value)
        self.assertEqual(3, self.linked_list.length)

    def test_prepend(self):
        self.linked_list.prepend(2)
        self.assertEqual(self.linked_list.get_head_value(), 2)
        self.assertEqual(self.linked_list.head.next.value, 3)
        self.assertEqual(self.linked_list.length, 2)
        self.assertEqual(self.linked_list.get_tail_value(), 3)

    def test_traverse_to_index(self):
        self.linked_list.append(4)
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.traverse_to(1).value, 4)
        self.assertEqual(self.linked_list.traverse_to(2).value, 5)

    def test_insert(self):
        self.linked_list.append(5)
        self.linked_list.insert(1, 4)
        self.assertEqual(self.linked_list.head.next.value, 4)
        self.assertEqual(self.linked_list.get_tail_value(), 5)
        self.assertEqual(self.linked_list.length, 3)
        self.assertListEqual(self.linked_list.to_list(), [3, 4, 5])

    def test_delete(self):
        self.linked_list.append(4)
        self.linked_list.append(5)
        self.linked_list.delete(1)
        self.assertListEqual(self.linked_list.to_list(), [3, 5])

    def test_delete_linked_list_with_1_node(self):
        self.linked_list.delete(0)
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.tail, None)

    def test_reverse_list(self):
        self.linked_list.append(4)
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.reverse()
        self.assertListEqual(self.linked_list.to_list(), [6, 5, 4, 3])
        self.assertFalse(self.linked_list.tail.next)
        self.assertEqual(self.linked_list.head.next.value, 5)
        self.assertEqual(self.linked_list.traverse_to(1).next.value, 4)

    def test_reverse_list_with_one_element(self):
        self.linked_list.reverse()
        self.assertListEqual(self.linked_list.to_list(), [3])

    def test_reverse_list_with_no_elements(self):
        self.linked_list.delete(0)
        self.linked_list.reverse()
        self.assertFalse(self.linked_list.length)


if __name__ == '__main__':
    unittest.main()
