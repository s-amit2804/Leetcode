class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def helper(i,j):
            if j>=len(t):
                return 1
            if i>=len(s):
                return 0
            if s[i]==t[j]:
                return (helper(i+1,j+1)+helper(i+1,j))
            return helper(i+1,j)
        return helper(0,0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna