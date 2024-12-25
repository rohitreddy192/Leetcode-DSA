class Solution {
    public int firstUniqChar(String s) {
        int[] mpp = new int[26];
        for(int i=0;i<s.length();i++){
            mpp[s.charAt(i)-'a'] += 1;
        }
        for(int i=0;i<s.length();i++){
            if(mpp[s.charAt(i)-'a']==1){
                return i;
            }
        }
        return -1;
    }
}