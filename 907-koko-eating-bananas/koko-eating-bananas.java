class Solution {
    private int sum(int[] piles){
        int maxi = 0;
        for(int i: piles){
            maxi = Math.max(i,maxi);
        }
        return maxi;
    }
    private boolean isPossible(int mid, int[] piles, int h){
        int total = 0;
        for(int i: piles){
            total += Math.ceil((double) i/mid);
        }
        return total<=h;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1, high = sum(piles);
        while(low<=high){
            int mid = (int) ((low+high)/2);
            if(isPossible(mid,piles,h)){
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        return low;
    }
}