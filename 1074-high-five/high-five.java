class Solution {
    public int[][] highFive(int[][] items) {
        Map<Integer, List<Integer>> mpp = new HashMap<>();
        for(int[] res : items){
            // if(mpp.containsKey(res[0])){
            //     mpp.get(res[0]).append(res[1])
            // }else{
            //     mpp.put(res[0], new ArrayList<Integer>())
            // }
            mpp.computeIfAbsent(res[0], k -> new ArrayList<>()).add(res[1]);
        }
        List<int[]> result = new ArrayList<>();
        mpp.forEach((key,values)->{
            Collections.sort(values,Collections.reverseOrder());
            int cnt = 0;
            for(int i=0;i<Math.min(values.size(),5);i++){
                cnt += values.get(i);
            }
            result.add(new int[]{key,cnt/5});
        });

        result.sort((a,b)-> Integer.compare(a[0],b[0]));
        return result.toArray(new int[result.size()][]);
    }
}