class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        l=0
        index=n
        r=n-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
                index=mid
            elif nums[mid]<target:
                l=mid+1
        return index

print(Solution().searchInsert([1,3,5,6],7))