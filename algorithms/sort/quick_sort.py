from Timer import timer


def partition(nums):
    pivot = nums[0]
    left, right = [], []
    for num in nums[1:]:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)
    return left, [pivot], right


def _quick_sort(nums):
    if len(nums) <= 1:
        return nums
    left, pivot, right = partition(nums)
    return _quick_sort(left) + pivot + _quick_sort(right)


@timer
def quick_sort(nums):
    return _quick_sort(nums)
