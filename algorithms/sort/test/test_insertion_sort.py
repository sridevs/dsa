import unittest
from insertion_sort import insertion_sort
from test.TestKit import TestKit


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.test_kit = TestKit(10, 100, 1000, 10000)

    def test_insertion_sort_for_a_tiny_input(self):
        expected = self.test_kit.tiny_set_of_n()
        input_nums = self.test_kit.tiny_sample_of_n()
        actual = insertion_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_insertion_sort_for_a_small_input(self):
        expected = self.test_kit.small_set_of_n()
        input_nums = self.test_kit.small_sample_of_n()
        actual = insertion_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_insertion_sort_for_a_medium_input(self):
        expected = self.test_kit.medium_set_of_n()
        input_nums = self.test_kit.medium_sample_of_n()
        actual = insertion_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_insertion_sort_for_a_large_input(self):
        expected = self.test_kit.large_set_of_n()
        input_nums = self.test_kit.large_sample_of_n()
        actual = insertion_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_insertion_sort_for_a_very_large_input(self):
        expected = self.test_kit.very_large_set_of_n()
        input_nums = self.test_kit.very_large_sample_of_n()
        actual = insertion_sort(input_nums)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
