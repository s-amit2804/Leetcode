class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        presum=[0 for i in range(0,len(nums))]
        for i in queries:
            presum[i[0]]+=1
            if i[1]<len(nums)-1:
                presum[i[1]+1]-=1
        for i in range(1,len(nums)):
            presum[i]+=presum[i-1]
        for i in range(0,len(nums)):
            if nums[i]>presum[i]:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna