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
    private int maxDiameter(TreeNode root, int[] arr){
        if(root == null) return 0;
        int left = maxDiameter(root.left, arr);
        int right = maxDiameter(root.right, arr);

        arr[0] = Math.max(left+right,arr[0]);

        return 1 + Math.max(left,right);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        int[] arr = {0};
        maxDiameter(root,arr);
        return arr[0];
    }
}