class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0;i<n-2;i++){
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int j=i+1, k=n-1;
            while(j<k && k<n){
                int sum = nums[j]+nums[k] + nums[i];
                if(sum == 0){
                    ans.add(new ArrayList<>(Arrays.asList(nums[i],nums[j],nums[k])));
                    j++;
                    while(j<n-1 && nums[j]==nums[j-1]) j++;
                    k--;
                    while(k>0 && nums[k]==nums[k+1]) k--;
                }
                else if(sum<0){
                    j++;
                }
                else{
                    k--;
                }
            }
        }
        return ans;
    }
}