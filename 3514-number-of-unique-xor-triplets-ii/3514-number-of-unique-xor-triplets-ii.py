class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s=set()
        nums=list(set(nums))
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                s.add(nums[i]^nums[j])
        s=list(s)
        res=set()
        for i in nums:
            for j in s:
                res.add(i^j)
        return len(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna