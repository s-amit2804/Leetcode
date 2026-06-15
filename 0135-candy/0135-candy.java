class Solution {
    public int candy(int[] ratings) {
        int[] res1=new int[ratings.length];
        res1[0]=1;
        int r=0;
        for(int i=1;i<ratings.length;i++){
            if(ratings[i]>ratings[i-1]){
                res1[i]=res1[i-1]+1;

            }
            else{
                res1[i]=1;
            }
        }
        int[] res2=new int[ratings.length];
        res2[ratings.length-1]=res1[ratings.length-1];
        for(int i=ratings.length-2;i>=0;i--){
            if(ratings[i]>ratings[i+1]){
                res2[i]=Math.max(res1[i],res2[i+1]+1);

            }
            else{
                res2[i]=res1[i];
            }
            
            r+=res2[i];
        }
        r+=res2[ratings.length-1];
        return r;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna