class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            if n%(i+1)==0:
                res+=nums[i]**2
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna