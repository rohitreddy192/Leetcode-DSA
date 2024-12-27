class Solution {
    public static Boolean isPalindrome(String s,int i, int j){
        while(i<=j){
            if(s.charAt(i)!=s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
    public String longestPalindrome(String s) {
        int maxi = 0;
        int n = s.length();
        if(n==1) return s;
        String ans = "" + s.charAt(0);
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(isPalindrome(s,i,j) && maxi<(j-i+1)){
                    maxi = j-i+1;
                    ans = s.substring(i,j+1);
                }
            }
        }
        return ans;
    }
}