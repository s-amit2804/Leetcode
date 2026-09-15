class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # @lru_cache(None)
        def ispalindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        @lru_cache(None)
        def dp(index):
            if index==len(s):
                return 0
            res=dp(index+1)
            for i in range(index+k-1,len(s)):
                if ispalindrome(index,i):
                    return max(res,1+dp(i+1))
            return res
        return dp(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna