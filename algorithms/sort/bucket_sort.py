from functools import reduce

from Timer import timer
from count_sort import concat_list
from insertion_sort import insertion_sort


@timer
def bucket_sort(nums):
    maximum = max(nums)
    bucket_size = int(len(nums)**0.5)
    buckets = [[] for _ in range(bucket_size+1)]
    for num in nums:
        pos = int((bucket_size * num) / maximum)
        buckets[pos].append(num)
    for bucket in buckets:
        buckets[buckets.index(bucket)] = insertion_sort(bucket)
    return reduce(concat_list, buckets)
