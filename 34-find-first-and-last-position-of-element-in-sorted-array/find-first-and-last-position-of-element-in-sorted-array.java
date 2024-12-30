class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int lowerbound = lowerBound(nums,n,target);
        int upperbound = upperBound(nums,n,target);
        if (lowerbound == n || nums[lowerbound] != target) {
            return new int[] {-1, -1};
        }
        return new int[]{lowerbound,upperbound-1};
    }

    private int lowerBound(int[] nums, int n, int target){
        int low = 0, high = n-1;
        int ans = n;
        while(low<=high){
            int mid = (low+high)/2;
            if(nums[mid]>=target){
                ans=mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return ans;

    }

    private int upperBound(int[] nums, int n, int target){
        int low = 0, high = n-1;
        int ans = n;
        while(low<=high){
            int mid = (low+high)/2;
            if(nums[mid]>target){
                ans=mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return ans;
    }


}