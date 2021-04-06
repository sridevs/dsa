import unittest

from ..doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.doubly_linked_list = DoublyLinkedList(3)


class TestOperations(TestDoublyLinkedList):
    def test_append(self):
        self.doubly_linked_list.append(4)
        self.assert_list_is([3, 4])
        self.assertEqual(self.doubly_linked_list.tail.prev.value, 3)

    def test_prepend(self):
        self.doubly_linked_list.prepend(2)
        self.assert_list_is([2, 3])
        self.assertEqual(self.doubly_linked_list.tail.prev.value, 2)

    def assert_list_is(self, lst):
        self.assertListEqual(self.doubly_linked_list.get_list(), lst)

    def test_insert(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.insert(1, 4)
        self.assert_list_is([3, 4, 5])
        self.assertEqual(self.doubly_linked_list.tail.prev.value, 4)
        self.assertEqual(self.doubly_linked_list.traverse_to(1).prev.value, 3)

    def test_delete(self):
        self.doubly_linked_list.append(4)
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(6)
        self.doubly_linked_list.delete(2)
        self.assert_list_is([3, 4, 6])
        self.assertEqual(self.doubly_linked_list.tail.prev.value, 4)

    def test_delete_tail(self):
        self.doubly_linked_list.append(4)
        self.doubly_linked_list.delete(1)
        self.assert_list_is([3])

    def test_delete_head(self):
        self.doubly_linked_list.append(4)
        self.doubly_linked_list.delete(0)
        self.assert_list_is([4])
        self.assertEqual(self.doubly_linked_list.head.prev, None)

    def test_reverse(self):
        self.doubly_linked_list.append(4)
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(6)
        # self.assert_list_is([3, 4, 5, 6])
        self.doubly_linked_list.reverse()
        self.assert_list_is([6, 5, 4, 3])
        self.assertEqual(4, self.doubly_linked_list.tail.prev.value)
        self.assertEqual(self.doubly_linked_list.traverse_to(1).prev.value, 6)
