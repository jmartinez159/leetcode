public class Solution {
    public int ScoreOfString(string s) {
        
        List<int> vals = new List<int>();
        int res = 0;
        for(int i = 0; i < s.Length-1; i++){

            int c1 = s[i];
            int c2 = s[i+1];
            vals.Add(Math.Abs(c1-c2));
        }
        
        for(int i = 0; i < vals.Count; i++){

            res += vals[i];
        }
        return res;
    }
}