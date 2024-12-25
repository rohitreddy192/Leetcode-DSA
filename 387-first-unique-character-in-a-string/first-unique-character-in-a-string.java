class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer> mpp = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char tmp = s.charAt(i);
            if(mpp.containsKey(tmp)){
                mpp.put(tmp, mpp.get(tmp)+1);
            }else{
                mpp.put(tmp,1);
            }
        }
        for(int i=0;i<s.length();i++){
            if(mpp.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
    }
}