import unittest
from quick_sort import quick_sort, partition
from test.TestKit import TestKit


class TestBuildMaxQuick(unittest.TestCase):

    def test_partition_given_odd_count_of_nums(self):
        actual = partition([3, 5, 1, 6, 0])
        expected = [6, 5, 1, 3, 0]
        self.assertListEqual(expected, actual)

    def test_partition_given_even_count_of_nums(self):
        actual = partition([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        self.assertListEqual(expected, actual)

    def test_partition_for_given_sample(self):
        actual = partition([1, 2, 0, 8, 9, 3, 5, 4, 7, 6])
        expected = [9, 8, 5, 7, 6, 3, 0, 4, 1, 2]
        self.assertListEqual(expected, actual)


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.test_kit = TestKit(10, 100, 1000, 10000, 100000, 100000000)

    def test_quick_sort_for_a_tiny_input(self):
        expected = self.test_kit.tiny_set_of_n()
        input_nums = self.test_kit.tiny_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_quick_sort_for_a_small_input(self):
        expected = self.test_kit.small_set_of_n()
        input_nums = self.test_kit.small_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_quick_sort_for_a_medium_input(self):
        expected = self.test_kit.medium_set_of_n()
        input_nums = self.test_kit.medium_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_quick_sort_for_a_large_input(self):
        expected = self.test_kit.large_set_of_n()
        input_nums = self.test_kit.large_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_quick_sort_for_a_very_large_input(self):
        expected = self.test_kit.very_large_set_of_n()
        input_nums = self.test_kit.very_large_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)

    def test_quick_sort_for_a_huge_input(self):
        expected = self.test_kit.huge_set_of_n()
        input_nums = self.test_kit.huge_sample_of_n()
        actual = quick_sort(input_nums)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
