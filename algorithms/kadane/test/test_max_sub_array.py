import unittest

from max_sub_array import max_sub_array


class TestMaxSubArray(unittest.TestCase):

    def test_max_sub_array_for_simple_sample(self):
        sample = [-4, -3, -2, 1, 2, 3, -5]
        expected = [1, 2, 3]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    def test_max_sub_array_for_all_positive_sample(self):
        sample = [4, 2, 3, 1]
        actual = max_sub_array(sample)
        self.assertListEqual(sample, actual)

    def test_max_sub_array_for_all_negative_sample(self):
        sample = [-3, -2, -9, -1]
        expected = [-1]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    @unittest.skip
    def test_max_sub_array_for_mixed_sample(self):
        sample = [5, -2, 7, 1, -9, 8, -3, 3, 1, -4, -8, 10]
        expected = [[5, -2, 7, 1], [5, -2, 7, 1, -9, 8, -3, 3, 1]]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    def test_max_sub_array_for_mixed_sum_is_max_sample(self):
        sample = [6, -1, 3, -2, 4, -1, 5, -2, 4]
        actual = max_sub_array(sample)
        self.assertListEqual(sample, actual)

    def test_max_sub_array_for_sample_with_single_largest(self):
        sample = [5, -2, 7, 1, -9, 8, -3, 3, 1, -4, -8, 100]
        expected = [100]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    @unittest.skip
    def test_max_sub_array_for_sample_with_multiple_maximums(self):
        sample = [-1, 1, 2, -3, 2, 1, -5]
        expected = [[1, 2], [2, 1]]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    def test_max_sub_array_for_single_pos_num_sample(self):
        sample = [10]
        actual = max_sub_array(sample)
        self.assertListEqual(sample, actual)

    def test_max_sub_array_for_single_neg_num_sample(self):
        sample = [-1]
        actual = max_sub_array(sample)
        self.assertListEqual(sample, actual)

    def test_max_sub_array_for_zero_max_sample(self):
        sample = [-2, -3, 0, -4, -1]
        expected = [0]
        actual = max_sub_array(sample)
        self.assertListEqual(expected, actual)

    def test_max_sub_array_for_empty_sample(self):
        sample = []
        actual = max_sub_array(sample)
        self.assertListEqual(sample, actual)
