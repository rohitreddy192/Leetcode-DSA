class Solution {
    private static String[] getPhnChars(){
        String[] phnChars = new String[10];
        phnChars[2]= "abc";
        phnChars[3] = "def";
        phnChars[4] = "ghi";
        phnChars[5] = "jkl";
        phnChars[6] = "mno";
        phnChars[7] = "pqrs";
        phnChars[8] = "tuv";
        phnChars[9] = "wxyz";
        return phnChars;
    }
    private void solve(String digits, int i, String currStr, List<String> res, Map<Character, String> d) {
        if (currStr.length() == digits.length()) {
            res.add(currStr);
            return;
        }
        
        // Get the possible letters for the current digit
        String letters = d.get(digits.charAt(i));
        for (char c : letters.toCharArray()) {
            solve(digits, i + 1, currStr + c, res, d);
        }
    }
    public List<String> letterCombinations(String digits) {
        Map<Character, String> d = new HashMap<>();
        d.put('2', "abc");
        d.put('3', "def");
        d.put('4', "ghi");
        d.put('5', "jkl");
        d.put('6', "mno");
        d.put('7', "pqrs");
        d.put('8', "tuv");
        d.put('9', "wxyz");
        
        List<String> res = new ArrayList<>();
        
        if (!digits.isEmpty()) {
            solve(digits, 0, "", res, d);
        }
        
        return res;
    }
}