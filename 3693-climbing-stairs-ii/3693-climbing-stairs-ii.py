class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs.append(0)
        costs.append(0)
        costs.append(0)
        @cache
        def helper(i):
            if i>=n:
                return 100000000
            if  i==n-1:
                return 0
            return min(helper(i+1)+costs[i+1]+1,helper(i+2)+costs[i+2]+4,helper(i+3)+costs[i+3]+9)
        return helper(-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna