class Solution {
    public int trap(int[] heights) {
        int n = heights.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        prefix[0] = heights[0];
        suffix[n-1] = heights[n-1];
        for(int i =1;i<n;i++){
            prefix[i] = prefix[i-1]>heights[i] ? prefix[i-1] : heights[i];
        }
        for(int i=n-2;i>=0;i--){
            suffix[i] = suffix[i+1]>heights[i] ? suffix[i+1] : heights[i];
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            ans += (Math.min(prefix[i],suffix[i])-heights[i]);
        }
        return ans;
    }
}