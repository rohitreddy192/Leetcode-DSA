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
class Tuple{
    int num;
    TreeNode node;
    public Tuple(TreeNode node, int num){
        this.node = node;
        this.num = num;
    }
}

class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        int[] arr = {0};
        Queue<Tuple> queue = new LinkedList<>();
        TreeMap<Integer,PriorityQueue<Integer>> map = new TreeMap<>();
        queue.offer(new Tuple(root,0));
        int ans = 0;
        while(!queue.isEmpty()){
            Tuple tuple = queue.peek();
            TreeNode node = tuple.node;
            int mmin = tuple.num;
            int size = queue.size();
            int first = 0, last = 0;
            for(int i=0;i<size;i++){
                int cur_id = queue.peek().num-mmin;
                node = queue.poll().node;
                if(i==0) first = cur_id;
                if(i==size-1) last = cur_id;
                if(node.left!=null) queue.offer(new Tuple(node.left,cur_id*2+1));
                if(node.right!=null) queue.offer(new Tuple(node.right,cur_id*2+2));
                }
            ans = Math.max(ans, last-first+1);
            }
        return ans;
    }
}