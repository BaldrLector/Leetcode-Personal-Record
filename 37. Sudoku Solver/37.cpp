class Solution {
public:
    bool row[9][10];
    bool col[9][10];
    bool grid[3][3][10];
    bool solve(vector<vector<char>>& board, int i, int j) {
        if (i>=9) return true;
        if (board[i][j] != '.')
            return solve(board,i+(j+1)/9,(j+1)%9);
        for (int k = 1; k<=9; k++) {
            if(!row[i][k] && !col[j][k] && !grid[i/3][j/3][k]) {
                board[i][j] = '0'+k;
                row[i][k] = true, col[j][k] = true, grid[i/3][j/3][k] = true;
                if(solve(board,i+(j+1)/9,(j+1)%9)) return true;
                board[i][j] = '.';
                row[i][k] = false, col[j][k] = false, grid[i/3][j/3][k] = false;
            }
        }
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        memset(grid, 0, sizeof(grid));
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if(board[i][j]!='.') {
                    row[i][board[i][j]-'0'] = true;
                    col[j][board[i][j]-'0'] = true;
                    grid[i/3][j/3][board[i][j]-'0'] = true;
                }
            }
        }
        solve(board, 0, 0);
    }
};