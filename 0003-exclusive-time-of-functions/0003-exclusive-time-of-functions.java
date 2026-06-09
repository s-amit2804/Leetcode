class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] res= new int[n];
        for(int i=0;i<res.length;i++){
            res[i]=0;
        }
        Deque<Integer> st = new ArrayDeque<>();
        for(String i:logs){
            String[] log = i.split(":");
            if(log[1].equals("start")){
                if(st.size()==0){
                    st.push(Integer.parseInt(log[0]));
                    res[Integer.parseInt(log[0])]-=Integer.parseInt(log[2]);
                }
                else{
                    res[(int)st.peek()]+=Integer.parseInt(log[2]);
                    st.push(Integer.parseInt(log[0]));
                    res[Integer.parseInt(log[0])]-=Integer.parseInt(log[2]);
                }
            }
            else{
                st.pop();
                res[Integer.parseInt(log[0])]+=Integer.parseInt(log[2])+1;
                if(st.size()>0){
                res[(int)st.peek()]-=Integer.parseInt(log[2])+1;
                }
            }
            for(int k=0;k<res.length;k++){
            System.out.print(res[k]);
                }

        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna