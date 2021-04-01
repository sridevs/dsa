from functools import reduce

from Timer import timer


def max_sum(acc, curr):
    max_now, max_moving = acc if type(acc) is tuple else (acc, acc)
    max_moving = max(curr, max_moving + curr)
    max_now = max(max_now, max_moving)
    return max_now, max_moving


@timer
def max_subarray_sum(nums):
    if len(nums) is 0:
        return 0
    if len(nums) is 1:
        return nums[0]
    max_now, max_moving = reduce(max_sum, nums)
    return max_now
