class Solution:
    def minOperations(self, n: int) -> int:
        res=0
        for i in range (1,n//2+1):
            res+=n-2*i+1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna