//problem : https://leetcode.com/problems/summary-ranges/submissions/938568984/

class Solution {
    public List<String> summaryRanges(int[] nums) {
        
        List<String> sol = new ArrayList<String>();
        if(nums.length == 0){

            return sol;
        }
        int i = 1;
        boolean flag = false;
        String ans = "" + nums[0];
        System.out.println(nums[0]);
        while(i < nums.length){

            if(nums[i-1]+1 != nums[i]){

                
                if(flag){

                    System.out.println(nums[i-1]);
                    
                    sol.add(new String(ans + "->" + nums[i-1]));
                    flag = false;
                }
                else{

                    sol.add(ans);
                }

                System.out.println(nums[i]);
                ans = new String(nums[i] + "");
            }
            else{

                flag = true;
            }
            
            i++;
        }

        if(flag){

              
            sol.add(new String(ans + "->" + nums[nums.length-1]));

        }

        else{

            sol.add(nums[nums.length-1] + "");
        }



        return sol;
    }
}
