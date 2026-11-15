class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd=0
        even=1
        res=0
        mod=1000000007
        sm=0
        for i in range(0,len(arr)):
            sm+=arr[i]
            if sm%2==0:
                even+=1
                res+=odd
            else:
                odd+=1
                res+=even
            res%=mod
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna