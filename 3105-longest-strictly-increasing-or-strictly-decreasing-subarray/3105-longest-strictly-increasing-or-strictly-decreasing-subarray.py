class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def dechelper(i):
            for j in range(i+1,len(nums)):
                if j!=0 and nums[j]>=nums[j-1]:
                    return j
            return len(nums)
        def inchelper(i):
            for j in range(i+1,len(nums)):
                if j!=0 and nums[j]<=nums[j-1]:
                    return j
            return len(nums)
        res=1
        i=0
        while i<len(nums):
            print(i)
            res=max(res,max(inchelper(i),dechelper(i))-i)
            i+=1
        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna