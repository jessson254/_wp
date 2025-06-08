def most_common(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    max_count = max(count.values())
    for num, c in count.items():
        if c == max_count:
            return num
