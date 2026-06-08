class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] res=new int[nums.length];
        int o=0;
        for(int i:nums){
            if(i<pivot){
                res[o]=i;
                o++;
            }
        }
        for(int i:nums){
            if(i==pivot){
                res[o]=i;
                o++;
            }
        }
        for(int i:nums){
            if(i>pivot){
                res[o]=i;
                o++;
            }
        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna