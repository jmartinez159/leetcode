public class Solution {
    public int[][] LargestLocal(int[][] grid) {
        
        int n = grid.Length;
        int[][] res = new int[n-2][];
        for(int i = 0; i < n-2; i++){
            res[i] = new int[n-2];
            for(int j = 0; j < n-2; j++){
                int curr = grid[i][j];
                for(int x = 0; x < 3; x++){
                    for(int y = 0; y < 3; y++){

                        curr = Math.Max(curr, grid[i+x][j+y]);
                    }
                }
                res[i][j] = curr;
            }
        }

        return res;
    }
}