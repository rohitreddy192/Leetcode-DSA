import java.util.*;

class Solution {
    public String intToRoman(int num) {
        // Create a LinkedHashMap to maintain insertion order
        Map<Integer, String> romanMap = new LinkedHashMap<>();
        romanMap.put(1000, "M");
        romanMap.put(900, "CM");
        romanMap.put(500, "D");
        romanMap.put(400, "CD");
        romanMap.put(100, "C");
        romanMap.put(90, "XC");
        romanMap.put(50, "L");
        romanMap.put(40, "XL");
        romanMap.put(10, "X");
        romanMap.put(9, "IX");
        romanMap.put(5, "V");
        romanMap.put(4, "IV");
        romanMap.put(1, "I");

        StringBuilder sb = new StringBuilder();

        // Iterate over the entries in the map
        for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
            int value = entry.getKey();
            String symbol = entry.getValue();

            // Append the Roman numeral symbol while num >= value
            while (num >= value) {
                num -= value;
                sb.append(symbol);
            }
        }

        return sb.toString();
    }
}
