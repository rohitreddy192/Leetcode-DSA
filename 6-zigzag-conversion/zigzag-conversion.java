class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1) return s;
        Map<Integer,List<Character>> mpp = new HashMap<>();
        int n = s.length();
        int rowTracker = 1;
        for(int i=0;i<numRows;i++){
            mpp.put(i,new ArrayList<>());
        }
        mpp.get(0).add(s.charAt(0));
        System.out.println(mpp);
        boolean flag = true;
        for(int i=1;i<n;i++){
            mpp.get(rowTracker).add(s.charAt(i));
            if(rowTracker==0 || rowTracker==numRows-1){flag = !flag;}
            if(flag) rowTracker++;
            if(!flag) rowTracker--;
        }

        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for (char c : mpp.get(i)) {
                result.append(c);
            }
        }

        return result.toString();
    }
}