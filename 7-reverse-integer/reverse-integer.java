class Solution {
    public int reverse(int x) {
        int temp = Math.abs(x);
        long revVal = 0;
        while(temp>0){
            revVal = revVal*10 + temp%10;
            temp = temp/10;
        }
         if (revVal >= Integer.MAX_VALUE || revVal <= Integer.MIN_VALUE) return 0;
        return (x>0)?(int) revVal:-1* (int) revVal;
    }
}