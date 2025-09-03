def binarySearch(arr,target):
    left = 0
    print(arr)
    right = len(arr)-1
    arr.sort()
    while(left<=right):
        mid = left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            left = mid+1
        elif arr[mid]<target:
            right=mid-1
    return -1

arr, target = list(eval(input("Enter the array: "))), int(input("Enter the target element: "))
if binarySearch(arr,target) == -1:
    print(f"The element {target} is not found in the array {arr}")
else:
    print(f"The element {target} is found in the array {arr} at index {binarySearch(arr, target)}")
    
# Q-704
# Leetcode
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return -1
