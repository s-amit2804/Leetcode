class Solution {
    public String frequencySort(String s) {
        HashMap<Character,Integer> hm=new HashMap<>();
        for(int i=0;i<s.length();i++){
            hm.put(s.charAt(i),1+hm.getOrDefault(s.charAt(i),0));
        }
        StringBuilder res=new StringBuilder();
        

        List<Map.Entry<Character, Integer>> list =
                new ArrayList<>(hm.entrySet());

        list.sort((a, b) -> b.getValue() - a.getValue());

        for (Map.Entry<Character, Integer> e : list) {
            for(int i=0;i<e.getValue();i++){
            res.append(e.getKey());
            }
        } 
        return res.toString();  
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna