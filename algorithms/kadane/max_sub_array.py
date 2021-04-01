from Timer import timer


@timer
def max_sub_array(nums):
    if len(nums) is 0:
        return nums
    in_max_subarray = False
    start_pos = 0
    max_sum = {'pos': start_pos, 'max': nums[start_pos]}
    max_so_far = nums[start_pos]
    for curr_poss in range(1, len(nums)):
        mov_sum = max_so_far + nums[curr_poss]
        max_so_far = max(nums[curr_poss], mov_sum)
        if max_so_far > max_sum.get('max'):
            max_sum = {'pos': curr_poss, 'max': max_so_far}
        if max_so_far is mov_sum and in_max_subarray is False:
            start_pos = curr_poss - 1
            in_max_subarray = True
        elif nums[curr_poss] is max_so_far and max_sum.get('pos') is curr_poss:
            start_pos = curr_poss
            in_max_subarray = False
    return nums[start_pos: max_sum.get('pos') + 1]
