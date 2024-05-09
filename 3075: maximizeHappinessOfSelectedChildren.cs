public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        
        Array.Sort(happiness);
        long res = 0;
        int picked = 0;
        int n = happiness.Length;
        while(n > 0 && k > 0){
            int curr = happiness[n-1-picked];
            if((curr - picked) <= 0){

                return res;
            }
            res += curr - picked;
            picked++;
            k--;
        }
        return res;
    }
}