class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> arr = new ArrayList<>();
        for(int i: nums1){
            arr.add(i);
        }
        for(int i:nums2){
            arr.add(i);
        }
        Collections.sort(arr);
        int n = arr.size();
        if(n==0) return 0;
        if(n==1) return arr.get(0);
        return n%2==0?((arr.get((n/2)-1) + arr.get(n/2)) / 2.0):arr.get(n/2);
    }
}