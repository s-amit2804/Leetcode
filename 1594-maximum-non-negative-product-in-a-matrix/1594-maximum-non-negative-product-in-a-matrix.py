class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        dp=[[[None,None] for i in range(len(grid[0]))] for j in range (len(grid))]
        dp[-1][-1]=[grid[-1][-1],grid[-1][-1]]
        def helper(i,j):
            if i==len(grid) or j==len(grid[0]):
                return [1000000000,-100000000]
            if dp[i][j]!=[None,None]:
                return dp[i][j]
            a=helper(i+1,j)
            b=helper(i,j+1)
            if grid[i][j]>0:
                dp[i][j]=[grid[i][j]*min(a[0],b[0]),grid[i][j]*max(a[1],b[1])]
            else:
                dp[i][j]=[grid[i][j]*max(a[1],b[1]),grid[i][j]*min(a[0],b[0])]
            return dp[i][j]
        a=helper(0,0)
        # print(dp)
        res= max(-1,a[0],a[1])
        if res>0:
            res=res%1000000007
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna