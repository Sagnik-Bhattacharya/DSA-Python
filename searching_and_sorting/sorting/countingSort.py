class Solution(object):
    def countingSort(self, nums):
        n = len(nums)
        mx = max(nums)
        # list size -> max number + 1
        freq = [0]*(mx+1)
        
        for i in nums:
            freq[i] += 1
        nums = []
        for i in range(0,mx+1):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1
        return nums

# Time complexity -> O(mx)
# Space complexity -> O(mx)

print(Solution().countingSort([12, 9, 31, 23, 45, 14]))