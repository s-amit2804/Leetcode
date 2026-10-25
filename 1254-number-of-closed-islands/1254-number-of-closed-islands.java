class Solution {
    public int closedIsland(int[][] grid) {
        for(int i=0;i<grid.length;i++){
            helper(grid,i,0);
            helper(grid,i,grid[0].length-1);
        }
        for(int i=0;i<grid[0].length;i++){
            helper(grid,0,i);
            helper(grid,grid.length-1,i);
        }
        int res=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==0){
                    res+=1;
                    helper(grid,i,j);
                }
            }
        }
        return res;
    }
    void helper(int[][] grid,int i,int j){
        if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j]==1){
            return;
        }
        grid[i][j]=1;
        helper(grid,i+1,j);
        helper(grid,i,j+1);
        helper(grid,i,j-1);
        helper(grid,i-1,j);
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna