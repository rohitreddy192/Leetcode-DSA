class Solution {
    public int maxArea(int[] height) {
        int maxi = 0;
        int n = height.length;
        int l=0, r = n-1;
        while(l<r){
            maxi = Math.max(maxi, Math.min(height[l],height[r])*(r-l));
            if(height[l]<height[r]){
                l++;
            }else{
                r--;
            }
        }
        return maxi;
    }
}