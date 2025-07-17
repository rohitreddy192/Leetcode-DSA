class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int j = 0, maxi = 0;
        for(int i=0;i< s.length();i++){
            while(j<i && set.contains(s.charAt(i))){
                set.remove(s.charAt(j));
                j++;
            }
            set.add(s.charAt(i));
            maxi = Math.max(i-j+1,maxi);
        }
        return maxi;
    }
}