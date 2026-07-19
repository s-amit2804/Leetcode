class Solution {
    public long maximumValue(int n, int s, int m) {
        if(n%2==1){
            n=n-1;        
    }
        long x=n;
        return s+(x/2)*m-(x-1)/2;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna