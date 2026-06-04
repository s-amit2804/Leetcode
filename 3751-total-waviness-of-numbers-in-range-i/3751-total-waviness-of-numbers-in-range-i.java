class Solution {
    public int totalWaviness(int num1, int num2) {
        int res=0;
        for(int i=num1;i<=num2;i++){
            res+=waviness(i);
        }
        return res;
    }
    public int waviness(int i){
        int res=0;
        if(i<=100){
            return res;
        }
        int past=i%10;
        i=i/10;
        int cur;
        int next;
        while(i>=10){
            cur=i%10;
            next=(i/10)%10;
            if((cur>past && cur>next) || (cur<past&& cur<next)){
                res+=1;
            }
            i=i/10;
            past=cur;
        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna