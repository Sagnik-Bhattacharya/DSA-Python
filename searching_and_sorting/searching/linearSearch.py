class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
print(Solution().search([-1,0,3,5,9,12],9))