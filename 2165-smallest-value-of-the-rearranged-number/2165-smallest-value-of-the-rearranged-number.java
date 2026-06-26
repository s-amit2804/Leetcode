class Solution {
    public long smallestNumber(long num) {
        if(num<0){
            num=-1*num;
            int[] dig= new int[10];
            for(int i=0;i<10;i++){
                dig[i]=0;
            }
            while(num>0){
                dig[(int)(num%10)]++;
                num=num/10;
            }
            long res=0;
            for(int i=9;i>=0;i--){
                while(dig[i]>0){
                    dig[i]--;
                    res=res*10+i;
                }
            }
            return -res;
        }
        else{
            int[] dig= new int[10];
            for(int i=0;i<10;i++){
                dig[i]=0;
            }
            while(num>0){
                // System.out.println(num);
                dig[(int)(num%10)]++;
                num=num/10;
            }
            long res=0;
            for(int i=1;i<10;i++){
                while(dig[i]>0){
                    dig[i]--;
                    res=res*10+i;
                    if(res>0){
                        while(dig[0]>0){
                            res=res*10;
                            dig[0]--;
                        }
                    }
                }
            }
            return res;
        }
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna