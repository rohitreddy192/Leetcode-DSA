class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) return s;

        // Use an array of StringBuilder for each row
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int rowTracker = 0; // To track the current row
        boolean goingDown = false; // Direction flag

        // Traverse the input string
        for (char c : s.toCharArray()) {
            rows[rowTracker].append(c); // Add the character to the current row

            // Change direction at the top or bottom row
            if (rowTracker == 0 || rowTracker == numRows - 1) {
                goingDown = !goingDown;
            }

            // Update the row index based on the direction
            rowTracker += goingDown ? 1 : -1;
        }

        // Combine all rows into a single result
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }
}
