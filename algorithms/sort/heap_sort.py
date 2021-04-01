from Timer import timer


@timer
def heap_sort(nums):
    build_max_heap(nums)
    for pos in range(len(nums)-1, 0, -1):
        exchange_pos(nums, 0, pos)
        max_heapify(nums, 1, pos)
    return nums


def build_max_heap(nums):
    mid_pos = int(len(nums) / 2)
    leaves = nums[:mid_pos]
    for pos in range(len(leaves)):
        max_heapify(nums, mid_pos - pos)
    return nums


def child_greater_than_parent(child_pos, parent_pos, nums, heap_size):
    return child_pos < heap_size and nums[child_pos] > nums[parent_pos]


def max_heapify(nums, pos, heap_size=0):
    left_pos, right_pos, largest = 2 * pos - 1, 2 * pos, pos - 1
    heap_size = heap_size or len(nums)
    if child_greater_than_parent(left_pos, largest, nums, heap_size):
        largest = left_pos
    if child_greater_than_parent(right_pos, largest, nums, heap_size):
        largest = right_pos
    if largest != pos - 1:
        exchange_pos(nums, pos - 1, largest)
        max_heapify(nums, largest + 1, heap_size)
    return nums


def exchange_pos(nums, pos1, pos2):
    nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
