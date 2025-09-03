# Template - 1
class Solution(object):
    def binarySearch(arr, target):
        left = 0
        right = len(arr)-1
        mid = left+(right-left)//2
        while(left<=right):
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
    
# 1. Simple and standard
# 2. Works best when it doesn't require  looking at it's neighbors
# 3. Only one index is checked at a time
# 4. Search condition is solely based on the current middle element(mid)

# Initial condition: left = 0, right=len(arr)-1
# Termination condition: left > right
# Mid calculation: mid = left + (right - left) // 2
# Search Left: right = mid - 1
# Search Right: left = mid + 1


# Template-2
class Solution(object):
    def condition(self,arr, num):
        pass
    def binarySearch_templateTwo(self, arr):
        left = 0
        right = len(arr)-1
        while(left<right):
            mid = left+(right-left)//2
            if self.condition(arr,mid):
                right = mid
            else:
                left=mid+1
        return left if self.condition(arr, left) else -1
    
