class Solution {
    public int orangesRotting(int[][] grid) {
        ArrayList<ArrayList<Integer>> arr=new ArrayList<>();
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==2){
                    arr.add(new ArrayList(Arrays.asList(i,j)));
                }
            }
        }
        int time=0;
        while(arr.size()>0){
            time++;
            int lim=arr.size();
            for(int x=0;x<lim;x++){
            int i=arr.get(0).get(0);
            int j=arr.get(0).get(1);
            arr.remove(0);
            if(i>0 && grid[i-1][j]==1){
                grid[i-1][j]==2;
                arr.add(new ArrayList(Arrays.asList(i-1,j)));
            }
            if(j>0 && grid[i][j-1]==1){
                grid[i][j-1]==2;
                arr.add(new ArrayList(Arrays.asList(i,j-1)));
            }
            if(i<grid.length-1 && grid[i+1][j]==1){
                grid[i+1][j]==2;
                arr.add(new ArrayList(Arrays.asList(i+1,j)));
            }
            if(j<grid[0].length-1 && grid[i][1+j]==1){
                grid[i][j+1]==2;
                arr.add(new ArrayList(Arrays.asList(i,1+j)));
            }
            }
        }
        return time;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna