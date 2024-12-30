class Pair {
    String word;
    int freq;

    public Pair(String word, int freq) {
        this.word = word;
        this.freq = freq;
    }
}

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> freqMap = new HashMap<>();
        for (String word : words) {
            freqMap.put(word, freqMap.getOrDefault(word, 0) + 1);
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((a,b)-> a.freq == b.freq ? a.word.compareTo(b.word) : b.freq - a.freq
        );
        
        for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
            pq.offer(new Pair(entry.getKey(), entry.getValue()));
        }

        List<String> result = new ArrayList<>();
        while (!pq.isEmpty() && k>0) {
            result.add(pq.poll().word);
            k -= 1;
        }
        return result;
    }
}