class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if k==1: return s==t
        if k==len(s): return True
        split_size = len(t)//k
        sub_arrays_t = [t[x:x+split_size] for x in range(0,len(t),split_size)]
        sub_arrays_s = [s[i:i + split_size] for i in range(0, len(s), split_size)]
        return Counter(sub_arrays_t) == Counter(sub_arrays_s)