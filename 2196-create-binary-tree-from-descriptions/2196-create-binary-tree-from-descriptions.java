/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode createBinaryTree(int[][] desc) {
        HashMap<Integer,TreeNode> hm=new HashMap<>();
        TreeNode parent,child;
        for(int i=0;i<desc.length;i++){
            if(hm.containsKey(desc[i][0])){
                parent=hm.get(desc[i][0]);
                if(hm.containsKey(desc[i][1])){
                    child=hm.get(desc[i][1]);
                }
                else{
                    child=new TreeNode(desc[i][1]);
                    hm.put(desc[i][1],child);
                }
            }
            else{
                parent=new TreeNode(desc[i][0]);
                hm.put(desc[i][0],parent);
                if(hm.containsKey(desc[i][1])){
                    child=hm.get(desc[i][1]);
                }
                else{
                    child=new TreeNode(desc[i][1]);
                    hm.put(desc[i][1],child);
                }
            }
            if(desc[i][2]==1){
                parent.left=child;
            }
            else{
                parent.right=child;
            }
        }
        for(int i=0;i<desc.length;i++){
            if(hm.containsKey(desc[i][1])){
                hm.remove(desc[i][1]);
            }
        }
        return hm.values().iterator().next();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna