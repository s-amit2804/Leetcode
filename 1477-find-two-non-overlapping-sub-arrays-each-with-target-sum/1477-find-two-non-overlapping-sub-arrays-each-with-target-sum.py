class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix=[1000000]*len(arr)
        sum=0
        d=dict()
        d[0]=-1
        for i in range(0,len(arr)):
            sum+=arr[i]
            if sum-target in d:
                prefix[i]=i-d[sum-target]
            prefix[i]=min(prefix[i],prefix[i-1])
            d[sum]=i
        suffix=[1000000]*len(arr)
        sum=0
        d.clear()
        d[0]=len(arr)
        for i in range(len(arr)-1,-1,-1):
            sum+=arr[i]
            if sum-target in d:
                suffix[i]=d[sum-target]-i
            suffix[i]=min(suffix[i],suffix[(i+1)%len(arr)])
            d[sum]=i
        res=1000000
        # print(prefix,suffix)
        for i in range(0,len(arr)-1):
            # print(suffix[i]+prefix[i])
            res=min(res,suffix[i+1]+prefix[i])
        if res==1000000:
            return -1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna