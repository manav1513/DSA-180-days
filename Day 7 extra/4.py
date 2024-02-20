def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + right // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    

    return left

print(searchInsert([1,2,3,4] ,5)) # 0

# nums1 = [1, 3, 5, 6]
# target1 = 5
# print(searchInsert(nums1, target1))

# def a(li,t):
#     l =0
#     r = len(li)-1
#     #print(l,r)
#     for i in range(0,len(li)):
#         mid = l + (r - l) // 2
#         #print(l, r, mid)
#         if li[mid] == t:
#             return mid
#         elif li[mid] < t:
#             l = mid
#             #print(left)
#         elif li[mid] > t:
#             r = mid
#     return l
# print(a([1,2,3,4],8))