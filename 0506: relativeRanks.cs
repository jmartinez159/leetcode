public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        
        List<int> ranks = new List<int> ();
        for(int i = 0; i < score.Length; i++){

            ranks.Add(score[i]);
        }

        ranks.Sort();
        Dictionary<int, string> rankMap = new Dictionary<int, string>();
        for(int i = 0; i < ranks.Count; i++){

            int curr = ranks[ranks.Count-1-i];
            if(i == 0){

                rankMap[curr] = "Gold Medal";
            }

            else if(i == 1){

                rankMap[curr] = "Silver Medal";
            }

            else if(i == 2){

                rankMap[curr] = "Bronze Medal";
            }

            else{

                int temp = i+1;
                rankMap[curr] = temp.ToString();
            }
        }

        string[] res = new string[score.Length];
        for(int i = 0; i < score.Length; i++){

            res[i] = rankMap[score[i]];
        }

        return res;
    }
}