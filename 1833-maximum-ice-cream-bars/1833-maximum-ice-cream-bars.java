class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int m=0;
        for(int i:costs){
            m=Math.max(m,i);
        }
        int[] csort= new int[m+1];
        for(int i=0;i<csort.length;i++){
            csort[i]=0;
        }
        for(int i:costs){
            csort[i]++;
        }
        for(int i=1;i<csort.length;i++){
            csort[i]+=csort[i-1];
        }
        int[] res=new int[costs.length];
        for(int i:costs){
            res[csort[i]-1]=i;
            csort[i]--;
        }
        int e=0;
        for(int i:res){
            if(i<=coins){
                e++;
                coins-=i;
            }
            else{
                break;
            }
        }
        return e;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna