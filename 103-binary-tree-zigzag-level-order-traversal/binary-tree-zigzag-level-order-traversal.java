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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<>();
        if(root == null) return res;
        queue.offer(root);
        boolean flag = false;
        while(!queue.isEmpty()){
            int qsize = queue.size();
            List<Integer> subList = new ArrayList<>();
            for(int i = 0; i<qsize;i++){
                TreeNode element = queue.poll();
                if(element.left != null) queue.offer(element.left);
                if(element.right != null) queue.offer(element.right);
                subList.add(element.val);
            }
            if(flag){
                Collections.reverse(subList);
            }
            flag = !flag;
            res.add(subList);
        }
        return res;
    }
}