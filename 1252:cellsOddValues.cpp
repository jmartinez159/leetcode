class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        
        int ans = 0;
        vector<vector<int>> table;
        vector<int> rows(n, 0);
        for(int i= 0; i < m; i++){

            table.push_back(rows);
        }

        for(int i = 0; i < indices.size(); i++){

            int rs = indices[i][0]; //rows
            int cs = indices[i][1]; //columns
            for(int j = 0; j < m; j++){
                table[j][cs]++;
            }

            for(int j = 0; j < n; j++){
                table[rs][j]++;
            }
        }

        for(int i = 0; i < m; i++){

            for(int j = 0; j < n; j++){

                if(table[i][j]%2 == 1){
                    ans++;
                }
            }
        }

        return ans;
    }
};