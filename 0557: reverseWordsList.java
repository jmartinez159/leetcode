// problem : https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution {
    public String reverseWords(String s) {
        
        String list[] = s.split(" ");
        String ans = "";
        char cur;

        for(int k = 0; k < list.length; k++){

            String x = list[k];
            for(int i = 0; i < x.length(); i++){

                cur = x.charAt(x.length()-1-i);
                ans = ans + cur;
            }

            if(k < list.length-1){

                ans = ans + " "; 
            }            
        }

        return ans;
    }
}
