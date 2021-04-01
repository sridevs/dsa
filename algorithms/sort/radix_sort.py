from functools import reduce

from Timer import timer
from count_sort import concat_list


def digit_sort(digit_pos, nums):
    place_holders = [[] for _ in range(10)]
    for num in nums:
        index = int(str(num)[digit_pos]) if abs(digit_pos) <= len(str(num)) else 0
        place_holders[index].append(num)
    return place_holders


def _radix_sort(nums, digit_pos=-1):
    sorted_nest = digit_sort(digit_pos, nums)
    if len([nums for nums in sorted_nest[1:] if nums != []]) is 0:
        return reduce(concat_list, sorted_nest)
    sorted_nums = reduce(concat_list, sorted_nest)
    digit_pos -= 1
    return _radix_sort(sorted_nums, digit_pos)


@timer
def radix_sort(nums):
    return _radix_sort(nums)
