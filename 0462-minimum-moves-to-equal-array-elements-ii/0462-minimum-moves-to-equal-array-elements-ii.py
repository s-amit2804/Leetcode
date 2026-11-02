class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return abs(nums[0]-nums[1])
        nums.sort()
        req=nums[len(nums)//2]
        areq=nums[len(nums)//2+1]
        res=0
        ares=0
        for i in nums:
            res+=abs(i-req)
            ares+=abs(i-areq)
        return min(res,ares)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna