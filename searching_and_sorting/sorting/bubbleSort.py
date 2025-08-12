class Solution(object):
    def bubbleSort(self, nums):
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swapped = True
            if(not swapped):
                break
        return nums
    # Space Complexity -> O(1)
    # Time Complexity -> Worst -> O(n^2)
    # Time Complexity -> Best -> O(n)
    
print(Solution().bubbleSort([22,13,44,15,21]))