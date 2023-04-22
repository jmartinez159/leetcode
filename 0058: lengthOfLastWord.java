//problem : https://leetcode.com/problems/length-of-last-word/submissions/

class Solution {
    public int lengthOfLastWord(String s) {
        
        String list[] = s.split(" ");

        return list[list.length-1].length();
    }
}
