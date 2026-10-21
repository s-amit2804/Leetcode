class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ngrid=[[0]*len(grid[0]) for i in range(0,len(grid))]
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                ngrid[i][j]=grid[i][j]
        p=1
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                ngrid[i][j]=p
                p=(p*grid[i][j])%12345
        p=1
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                grid[i][j],p=(p*ngrid[i][j])%12345,(p*grid[i][j])%12345
        return grid

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna