from functools import reduce
from itertools import repeat

from Timer import timer


def concat_list(list1, list2):
    list1.extend(list2)
    return list1


@timer
def count_sort(nums):
    place_holders = [[] for _ in range(len(nums))]
    for num in nums:
        place_holders[num].append(num)
    return reduce(concat_list, place_holders)

