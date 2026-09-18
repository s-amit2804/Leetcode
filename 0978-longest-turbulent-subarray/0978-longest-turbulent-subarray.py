class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        @cache
        def helper(index,prev,dir):
            if index==len(arr):
                return 0
            if dir==1:
                if arr[index]>prev:
                    return 1+helper(index+1,arr[index],-1)
                return 0
            if dir==-1:
                if arr[index]<prev:
                    return 1+helper(index+1,arr[index],1)
                return 0
            return 1+max(helper(index+1,arr[index],1),helper(index+1,arr[index],-1))
        res=0
        for i in range(0,len(arr)):
            res=max(res,helper(i,0,0))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna