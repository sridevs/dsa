from random import sample


class TestKit:

    def __init__(self, tiny_count, min_count, medium_count, large_count, very_large_count=100000, huge_count=1000000):
        self.tiny_nums_count = tiny_count
        self.small_nums_count = min_count
        self.medium_nums_count = medium_count
        self.large_nums_count = large_count
        self.very_large_nums_count = very_large_count
        self.huge_nums_count = huge_count
        self.tiny_range = range(self.tiny_nums_count)
        self.small_range = range(self.small_nums_count)
        self.medium_range = range(self.medium_nums_count)
        self.large_range = range(self.large_nums_count)
        self.very_large_range = range(self.very_large_nums_count)
        self.huge_range = range(self.huge_nums_count)

    def tiny_set_of_n(self):
        return list(self.tiny_range)

    def small_set_of_n(self):
        return list(self.small_range)

    def medium_set_of_n(self):
        return list(self.medium_range)

    def large_set_of_n(self):
        return list(self.large_range)

    def very_large_set_of_n(self):
        return list(self.very_large_range)

    def huge_set_of_n(self):
        return list(self.huge_range)

    def tiny_sample_of_n(self):
        return sample(self.tiny_range, self.tiny_nums_count)

    def small_sample_of_n(self):
        return sample(self.small_range, self.small_nums_count)

    def medium_sample_of_n(self):
        return sample(self.medium_range, self.medium_nums_count)

    def large_sample_of_n(self):
        return sample(self.large_range, self.large_nums_count)

    def very_large_sample_of_n(self):
        return sample(self.very_large_range, self.very_large_nums_count)

    def huge_sample_of_n(self):
        return sample(self.huge_range, self.huge_nums_count)
