import unittest
from merge_sort import divide_and_conquer, merge
from test.TestKit import TestKit


class TestMerge(unittest.TestCase):
    def test_merge_given_even_pair(self):
        actual = merge([3, 5, 6], [2, 4, 7])
        expected = [2, 3, 4, 5, 6, 7]
        self.assertListEqual(expected, actual)

    def test_merge_given_odd_pair(self):
        actual = merge([3, 5, 6], [2, 4, 7, 8])
        expected = [2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(expected, actual)

    def test_merge_given_largest_in_list1(self):
        actual = merge([3, 9], [0, 2, 5])
        expected = [0, 2, 3, 5, 9]
        self.assertListEqual(expected, actual)

    def test_merge_given_largest_in_list2(self):
        actual = merge([3, 4], [0, 2, 5])
        expected = [0, 2, 3, 4, 5]
        self.assertListEqual(expected, actual)

    def test_merge_given_mixed_values1(self):
        actual = merge([1, 5], [0, 6, 7])
        expected = [0, 1, 5, 6, 7]
        self.assertListEqual(expected, actual)

    def test_merge_given_mixed_values2(self):
        actual = merge([2, 3, 4, 8, 9], [0, 1, 5, 6, 7])
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(expected, actual)


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.test_kit = TestKit(10, 100, 1000, 10000, 100000, 1000000)

    def test_merge_sort_for_a_tiny_input(self):
        expected = self.test_kit.tiny_set_of_n()
        input_nums = self.test_kit.tiny_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)

    def test_merge_sort_for_a_small_input(self):
        expected = self.test_kit.small_set_of_n()
        input_nums = self.test_kit.small_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)

    def test_merge_sort_for_a_medium_input(self):
        expected = self.test_kit.medium_set_of_n()
        input_nums = self.test_kit.medium_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)

    def test_merge_sort_for_a_large_input(self):
        expected = self.test_kit.large_set_of_n()
        input_nums = self.test_kit.large_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)

    def test_merge_sort_for_a_very_large_input(self):
        expected = self.test_kit.very_large_set_of_n()
        input_nums = self.test_kit.very_large_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)

    def test_merge_sort_for_a_huge_input(self):
        expected = self.test_kit.huge_set_of_n()
        input_nums = self.test_kit.huge_sample_of_n()
        actual = divide_and_conquer(input_nums)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
