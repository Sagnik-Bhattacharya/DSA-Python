class Solution:
    def check(self,m, target):
        return m>target
    def upperBound(self, arr, target):
        # code here
        n=len(arr)
        if arr[-1]<target:
            return n
        l=0
        r=n-1
        while(r-l>1):
            m=(l+r)//2
            if(self.check(arr[m],target)):
                r=m
            else:
                l=m
        return r
        
print(Solution().upperBound([2,3,7,10,11,11,25],9))