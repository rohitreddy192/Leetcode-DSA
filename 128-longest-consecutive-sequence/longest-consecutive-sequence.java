class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        for(int num:nums){
            hashSet.add(num);
        }
        int maxLen = 0;
        for(int num: nums){
            if(!hashSet.contains(num-1)){
                int cnt = 1;
                while(hashSet.contains(num+1)){
                    cnt += 1;
                    num += 1;
                }
                maxLen = Math.max(maxLen,cnt);
            }
        }
        return maxLen;
    }
}