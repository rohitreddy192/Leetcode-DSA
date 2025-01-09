class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum = 0;
        Map<Integer,Integer> mpp = new HashMap<>();
        mpp.put(0,1);
        int cnt = 0;
        for(int num: nums){
            sum += num;
            if(mpp.containsKey(sum-k)) cnt += mpp.get(sum-k);

            mpp.put(sum, mpp.getOrDefault(sum,0)+1);
        }
        return cnt;
    }
}