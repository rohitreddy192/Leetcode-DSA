class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }

            int j = i+1, k = n-1;
            while(j<k){
                if(nums[i]+nums[j]+nums[k]==0){
                    res.add(List.of(nums[i],nums[j],nums[k]));
                    j++;
                    k--;
                    while(j<k && nums[j]==nums[j-1]){
                        j++;
                    }
                    while(j<k && nums[k]==nums[k+1]){
                        k--;
                    }
                } else if(nums[i]+nums[j]+nums[k] < 0){
                    j++;
                    while(j<k && nums[j]==nums[j-1]){
                        j++;
                    }
                }else{
                    k--;
                    while(j<k && nums[k]==nums[k+1]){
                        k--;
                    }
                }
            }
        }
        return res;
    }
}