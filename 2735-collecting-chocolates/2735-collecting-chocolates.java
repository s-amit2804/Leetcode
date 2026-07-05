class Solution {
    public long minCost(int[] nums, long cost) {
        long res=0;
        int[] minn=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            res+=nums[i];
            minn[i]=nums[i];
        }
        for(int i=0;i<nums.length;i++){
            long x=cost*i;
            for(int j=0;j<nums.length;j++){
                minn[j]=Math.min(nums[Math.abs((j+i)%nums.length)],minn[j]);
                x+=Math.min(nums[Math.abs((j+i)%nums.length)],minn[j]);
            }
            res=Math.min(res,x);
        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna