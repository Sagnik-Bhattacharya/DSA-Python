class Solution(object):
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            mpos = i
            for j in range(i+1,n):
                if nums[j] < nums[mpos]:
                    mpos = j
            nums[i],nums[mpos] = nums[mpos],nums[i]
        return nums
    
    # Space Complexity -> O(1)
    # Time Complexity -> O(n^2) -> Worst Case
    # Time Complexity -> O(n^2) -> Best Case
    
print(Solution().selectionSort([22,13,44,15,21]))