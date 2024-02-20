def missingNumber(nums):

    nums.sort()
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i

print(missingNumber([3,0,1]))  
        