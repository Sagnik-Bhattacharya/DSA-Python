class Solution(object):
    def partition(self, nums, l, r):
        key = nums[r]
        start = l
        for i in range(l, r + 1):
            if nums[i] <= key:
                nums[i], nums[start] = nums[start], nums[i]  # Swap properly
                start += 1
        return start - 1

    def quickSort(self, nums, l, r):
        if l >= r:  # Base case added
            return
        p = self.partition(nums, l, r)
        self.quickSort(nums, l, p - 1)
        self.quickSort(nums, p + 1, r)

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

'''Your partition logic is doing an in-place Lomuto partition (which is fine).

You mentioned space complexity is O(1), which is true except for the recursion stack: it becomes O(log n) in best case, O(n) in worst case.

The time complexity:

Best/Average case: O(n log n)

Worst case: O(n²) (when array is already sorted or reverse sorted and pivot is poorly chosen)'''
print(Solution().sortArray([12, 9, 31, 23, 45, 14]))
