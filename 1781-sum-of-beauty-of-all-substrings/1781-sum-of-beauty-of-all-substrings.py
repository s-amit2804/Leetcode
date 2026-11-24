class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(0,n):
            freq=[0]*26
            for j in range(i,n):
                freq[ord(s[j])-ord("a")]+=1
                res+=max(freq)-min([i for i in freq if i>0])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna