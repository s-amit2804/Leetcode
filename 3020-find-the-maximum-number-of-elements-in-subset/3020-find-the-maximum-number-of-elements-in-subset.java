class Solution {
    public int maximumLength(int[] nums) {
        HashMap<Integer,Integer> hm=new HashMap<>();
        for (int num : nums) {
            hm.put(num, hm.getOrDefault(num, 0) + 1);
        }
        int res=hm.getOrDefault(1,1);
        if(res%2==0){
            res--;
        }
        int c=0,cnt=0;
        for(int i:hm.keySet()){
            if(i!=1){
                c=i;
                cnt=0;
                while(hm.getOrDefault(c,0)>=2){
                    cnt++;
                    c=c*c;
                }
                // System.out.println(i+ " "+ c);
                if(hm.getOrDefault(c,0)==1){
                    res=Math.max(res,cnt*2+1);
                }
                else{
                    res=Math.max(res,cnt*2-1);
                }

            }
        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna