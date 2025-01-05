class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int total = 0;
        for(int i=0;i<s.length()-1;i++){
            if(romanMap.get(s.charAt(i)) < romanMap.get(s.charAt(i+1))){
                total -= romanMap.get(s.charAt(i));
            }else{
                total += romanMap.get(s.charAt(i));
            }
        }
        return total + romanMap.get(s.charAt(s.length()-1));
    }
}