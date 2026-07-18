class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int[] res= new int[nums.length-k+1];
        for(int i=k-1;i<nums.length;i++){
            if(helper(i-k+1,i,nums)){
                res[i-k+1]=nums[i];
            }
            else{
                res[i-k+1]=-1;
            }
        }
        return res;
    }
    public boolean helper(int st,int en , int[]nums){
        for(int i=st+1;i<en+1;i++){
            // System.out.print(st);
            if (nums[i]!=nums[i-1]+1){
                return false;
            }
        }
        return true;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna