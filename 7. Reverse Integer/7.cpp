class Solution {
public:
    int reverse(int x) {
        long long j = 0;
    	do{
    		j = j * 10 + x % 10;
    	}while (x /= 10);
        return (j > INT_MAX || j < INT_MIN) ? 0: (int)j;
    }
};
