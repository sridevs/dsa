import unittest

from datastructures.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue("person1")


class TestInit(TestQueue):
    def test_person1_is_added(self):
        self.assertTrue(self.queue.head, "person1")

    def test_head_and_tail_are_same(self):
        self.assertTrue(self.queue.head is self.queue.tail)

    def test_length_of_queue_is_1(self):
        self.assertTrue(1, self.queue.length)


class TestOperation(TestQueue):
    def test_peek(self):
        self.assertTrue(self.queue.peek() is self.queue.head)

    def test_enqueue(self):
        # print(self.queue.head)
        self.queue.enqueue("person2")
        self.queue.enqueue("person3")
        self.assertEqual(self.queue.peek().value, "person1")
        self.assertEqual(self.queue.peek().next.value, "person2")

    def test_enqueue_for_empty_queue(self):
        empty_queue = Queue()
        person1 = "person1"
        empty_queue.enqueue(person1)
        self.assertEqual("person1", empty_queue.head.value, empty_queue.tail.value)

    def test_dequeue(self):
        self.queue.enqueue("person2")
        self.queue.enqueue("person3")
        self.assertTrue(self.queue.head is self.queue.dequeue())
        self.queue.dequeue()
        self.assertEqual(self.queue.head.value, self.queue.tail.value, "person3")
        self.queue.dequeue()
        self.assertTrue(self.queue.head is self.queue.tail is None)


if __name__ == '__main__':
    unittest.main()