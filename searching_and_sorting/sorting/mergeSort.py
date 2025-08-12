class Solution(object):
    def merge(self, arr, l, mid, r):
        a = [x for x in arr[l:mid+1]]
        b = [x for x in arr[mid+1: r+1]]
        i, j, k = 0, 0, l
        while k <= r:
            if j == len(b):
                arr[k] = a[i]
                i += 1
            elif i == len(a):
                arr[k] = b[j]
                j += 1
            elif a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1

    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        self.merge(nums, l, mid, r)

    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums  # You were missing this line to return the sorted array

print(Solution().sortArray([12, 9, 31, 23, 45, 14]))

# Space complexity -> O(n)
# Time complexity -> O(nlogn)