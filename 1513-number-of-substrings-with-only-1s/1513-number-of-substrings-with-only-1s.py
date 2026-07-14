class Solution:
    def numSub(self, s: str) -> int:
        def helper(n):
            return (n*(n+1))//2
        res=0
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                c+=1
                res+=c
                res%=1000000007
            else:
                c=0
        return res
            
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna