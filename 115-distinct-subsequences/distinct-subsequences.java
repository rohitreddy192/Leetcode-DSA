class Solution {
    private int solve(int i, int j,  String s, String t, int[][] dp){
        if(j>=t.length()){
            return 1;
        }
        
        if(i>=s.length() && j<t.length()){
            return 0;
        }

        if(dp[i][j]!= -1) return dp[i][j];

        int pick = 0;
        int not_pick = 0;
        if(s.charAt(i) == t.charAt(j)){
            pick = solve(i+1,j+1,s,t,dp) + solve(i+1,j,s,t,dp);
        }else{
            not_pick = solve(i+1,j,s,t,dp);
        }

        return pick + not_pick;

    }

    public int numDistinct(String s, String t) {
        s = " "+ s;
        t = " "+ t;
        int n = s.length();
        int m = t.length();
        int[][] dp = new int[s.length()][t.length()];
        for(int i=0;i<n;i++){
            dp[i][0] = 1;
        }
        for(int i=1; i<n;i++){
            for(int j=1;j<m;j++){
                if(s.charAt(i)==t.charAt(j))
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[n-1][m-1];
    }
}