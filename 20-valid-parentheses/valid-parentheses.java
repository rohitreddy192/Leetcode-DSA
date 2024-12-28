class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            Character tmp = s.charAt(i);
            if(!stack.isEmpty() && ((tmp.equals('}') && stack.peek().equals('{')) || (tmp.equals(')') && stack.peek().equals('(')) || (tmp.equals(']') && stack.peek().equals('[')))) stack.pop();
            else{
                stack.push(tmp);
            }
        }
        return stack.isEmpty();
    }
}