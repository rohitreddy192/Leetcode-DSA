class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            for(int j=i+1;j<n;j++){
                if(j>i+1 && nums[j]== nums[j-1]) continue;
                int left = j+1, right = n - 1;
                while(left<right){
                    long totalSum =(long)nums[i] + nums[j] + nums[left] + nums[right];
                    if(totalSum > target){
                        right--;
                    }
                    else if(totalSum < target){
                        left++;
                    }
                    else{
                       ans.add(new ArrayList<>(Arrays.asList(nums[i],nums[j],nums[left],nums[right])));
                        left++;
                        right--;
                        while(left<right && nums[left]==nums[left-1]) left++;
                        while(left<right && nums[right]==nums[right+1]) right--;
                    }
                }
            }
        }
        return ans;
    }
}