from Timer import timer


def append(list1, list2, pos):
    list1.append(list2[pos])
    pos += 1
    return pos


def merge(left, right):
    result = []
    left_pos, right_pos = 0, 0
    for _ in left + right:
        if left_pos >= len(left):
            right_pos = append(result, right, right_pos)
        elif right_pos >= len(right) or left[left_pos] <= right[right_pos]:
            left_pos = append(result, left, left_pos)
        else:
            right_pos = append(result, right, right_pos)

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_pos = int(len(nums) / 2)
    left = merge_sort(nums[:mid_pos])
    right = merge_sort(nums[mid_pos:])
    return merge(left, right)


@timer
def divide_and_conquer(nums):
    return merge_sort(nums)
