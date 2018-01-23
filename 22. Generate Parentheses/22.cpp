class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        addingpar(res, "", n, 0);
        return res;
    }
    void addingpar(vector<string> &v, string str, int n, int m){
        if(n==0 && m==0) {
            v.push_back(str);
            return;
        }
        if(m > 0){ addingpar(v, str+")", n, m-1); }
        if(n > 0){ addingpar(v, str+"(", n-1, m+1); }
    }
};


//dp
//dp[0] = ""
//dp[i]='('+ dp[k]+')'+dp[i-1-k],k=0..i-i
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector< vector<string> > dp(n+1, vector<string>());
        dp[0].push_back("");
        for(int i=1; i<=n; ++i){
            for(int k=0; k<i; ++k){
                for(string s1: dp[k]){
                    for(string s2: dp[i-1-k])
                        dp[i].push_back("("+s1+")"+s2);
                }
            }
        }
        return dp[n];
    }
};

