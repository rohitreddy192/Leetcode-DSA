class Solution {
    private int solve(int i, int j, String s, String t, int[][] dp){
        if(j==t.length()) return s.length()-i;
        if(i==s.length()) return t.length()-j;

        if(dp[i][j] != -1) return dp[i][j];
        int insert =0, delete = 0,replace = 0;
        if(s.charAt(i)==t.charAt(j)){
            return solve(i+1,j+1,s,t,dp);
        }else{
            insert = solve(i,j+1,s,t,dp);
            delete = solve(i+1,j,s,t,dp);
            replace = solve(i+1,j+1,s,t,dp);
            return dp[i][j] = 1 + Math.min(insert, Math.min(delete,replace));
        }
    }
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()][word2.length()];
        for(int i=0;i<word1.length();i++){
            Arrays.fill(dp[i],-1);
        }
        return solve(0,0,word1,word2,dp);
    }
}