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
    private int pathSum(TreeNode root, int[] arr){
        if(root == null) return 0;

        int leftSum = Math.max(0,pathSum(root.left, arr));
        int rightSum = Math.max(0,pathSum(root.right, arr));

        arr[0] = Math.max(arr[0], rightSum + leftSum + root.val );

        return root.val + Math.max(leftSum,rightSum);
    }
    public int maxPathSum(TreeNode root) {
        if(root==null) return 0;
        int[] arr = {root.val};
        pathSum(root,arr);
        return arr[0];
    }
}