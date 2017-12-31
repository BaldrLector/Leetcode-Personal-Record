class Solution {
public:
    bool isPalindrome(int x) {
        int rem, rev=0;
        if(x<0)
            return false;
        if(x==0)
            return true;
        int y=x;
        while(x != 0)
        {
            rem=x%10;
            rev=rev*10+rem;
            x=x/10;
        }
        if(y==rev)
            return true;
        else
            return false;
    }
};