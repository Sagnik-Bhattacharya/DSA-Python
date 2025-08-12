class Solution(object):
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(n):
            key = nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key
        return nums

    # Space Complexity -> O(1)
    # Time Complexity -> O(n^2) -> Worst and O(n) -> Best
    
print(Solution().insertionSort([22,13,44,15,21]))