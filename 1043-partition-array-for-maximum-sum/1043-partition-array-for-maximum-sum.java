class Solution {
    int[] dp;

    public int helper(int index, int[] arr, int k) {

        if (index >= arr.length) {
            return 0;
        }
        if (dp[index] != -1) {
            return dp[index];
        }
        int mx = arr[index];
        int res = mx;
        for (int i = 0; i < Math.min(arr.length - index, k); i++) {
            mx = Math.max(mx, arr[index + i]);
            res = Math.max(res, mx * (i + 1) + helper(index + i + 1, arr, k));
        }
        dp[index] = res;
        return res;
    }

    public int maxSumAfterPartitioning(int[] arr, int k) {
        dp = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            dp[i] = -1;
        }
        return helper(0, arr, k);
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna