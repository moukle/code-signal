def containsCloseNums(nums, k):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            if i - dict[nums[i]] <= k:
                return True
        dict[nums[i]] = i
    return False