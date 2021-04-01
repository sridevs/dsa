from Timer import timer


# @timer
def insertion_sort(nums):
    sorted_nums = nums[:1]
    for num in nums[1:]:
        insert_at = 0
        while insert_at < len(sorted_nums) and num >= sorted_nums[insert_at]:
            insert_at += 1
        sorted_nums.insert(insert_at, num)
    return sorted_nums
