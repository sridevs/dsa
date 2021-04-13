import unittest

from datastructures.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack("plate1")


class TestInit(TestStack):
    def test_head_and_tail_are_same(self):
        self.assertTrue(self.stack.head is self.stack.tail)
        self.assertTrue(self.stack.head, "plate1")


class TestOperation(TestStack):
    def test_peek(self):
        self.assertTrue(self.stack.peek() is self.stack.head)

    def test_push(self):
        self.stack.push("plate2")
        self.stack.push("plate3")
        self.assertEqual(self.stack.peek().value, "plate3")
        self.assertEqual(self.stack.peek().next.value, "plate2")

    def test_pop(self):
        self.stack.push("plate2")
        self.stack.push("plate3")
        self.assertTrue(self.stack.head is self.stack.pop())
        self.stack.pop()
        self.assertEqual(self.stack.head.value, self.stack.tail.value, "plate1")
        self.stack.pop()
        self.assertTrue(self.stack.head is self.stack.tail is None)
