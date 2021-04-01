from Timer import timer


def swap_pos(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


@timer
def bubble_sort(nums):
    for _ in nums[:-1]:
        slice_at_end = -1
        for current_pos in range(len(nums[:slice_at_end])):
            next_pos = current_pos + 1
            if nums[current_pos] > nums[next_pos]:
                swap_pos(nums, current_pos, next_pos)
            slice_at_end -= 1
    return nums
