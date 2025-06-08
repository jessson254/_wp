def average(nums):
    if not nums:
        return 0
    avg = sum(nums) / len(nums)
    return round(avg, 1)
