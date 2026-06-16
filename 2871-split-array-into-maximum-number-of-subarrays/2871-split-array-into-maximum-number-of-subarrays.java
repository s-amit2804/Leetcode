class Solution {
    public int maxSubarrays(int[] nums) {
        // int m=nums[0];
        int c=0;
        // for(int i:nums){
        //     m=
        // }
        // if(c==0){
        //     return 1;
        // }
        c=0;
        int x=2048*2048-1;
        for(int i=0;i<nums.length;i++){
            x=x&nums[i];
            if(x==0){
                c++;
                x=2048*2048-1;
            }
        }
        if(c==0){
            return 1;
        }
        return c;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna