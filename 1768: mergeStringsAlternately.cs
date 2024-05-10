public class Solution {
    public string MergeAlternately(string word1, string word2) {
        string res = "";
        int i = 0;
        while(i < word1.Length && i < word2.Length){

            res += word1[i];
            res += word2[i];
            i++;
        }

        while(i < word1.Length){

            res += word1[i];
            i++;
        }

        while(i < word2.Length){

            res += word2[i];
            i++;
        }

        return res;
    }
}