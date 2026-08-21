class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        presum=[]
        for i in grid:
            presum.append([i[0]])
            for j in range(1,len(i)):
                presum[-1].append(presum[-1][-1]+i[j])
        # print(presum)
        for i in range(1,len(grid)):
            for j in range(0,len(grid[0])):
                presum[i][j]+=presum[i-1][j]
        res=0
        for i in presum:
            for j in i:
                if j<=k:
                    res+=1
        # print(presum)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna