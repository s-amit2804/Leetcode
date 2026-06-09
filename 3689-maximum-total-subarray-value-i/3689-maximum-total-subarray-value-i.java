class Solution {
    public long maxTotalValue(int[] nums, int k) {
        long maxx=0,minn=1000000001;
        for(long i:nums){
            if(i>maxx){
                maxx=i;
            }
            if(i<minn){
                minn=i;
            }
        }
        System.out.println(maxx+" "+minn);
        return (maxx-minn)*k;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna