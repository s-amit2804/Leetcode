class Solution:
    def distinctSubseqII(self, s: str) -> int:
        vis=[-1]*26
        dp=[0]*(len(s)+1)
        dp[0]=1
        mod=10**9+7
        for i in range(1,len(s)+1):
            dp[i]=(dp[i-1]*2)%mod
            index=ord(s[i-1])-ord('a')
            if vis[index]!=-1:
                dp[i]=(dp[i]-dp[vis[index]]+mod)%mod
            vis[index]=i-1
        return (dp[len(s)]-1)%mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna