After reading some good sharing solutions, I’d like to show them together. You can see different ideas in the code.

nest myPow
double myPow(double x, int n) {
    if(n<0) return 1/x * myPow(1/x, -(n+1));
    if(n==0) return 1;
    if(n==2) return x*x;
    if(n%2==0) return myPow( myPow(x, n/2), 2);
    else return x*myPow( myPow(x, n/2), 2);
}
double myPow
double myPow(double x, int n) { 
    if(n==0) return 1;
    double t = myPow(x,n/2);
    if(n%2) return n<0 ? 1/x*t*t : x*t*t;
    else return t*t;
}
double x
double myPow(double x, int n) { 
    if(n==0) return 1;
    if(n<0){
        n = -n;
        x = 1/x;
    }
    return n%2==0 ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
}
iterative one
double myPow(double x, int n) { 
    if(n==0) return 1;
    if(n<0) {
        n = -n;
        x = 1/x;
    }
    double ans = 1;
    while(n>0){
        if(n&1) ans *= x;
        x *= x;
        n >>= 1;
    }
    return ans;
}

bit operation

class Solution {
public:
    double myPow(double x, int n) {
    	if(n<0){
    		x = 1.0/x;
    		n = -n;
    	}
    	int unsigned m = n;
        double tbl[32] = {0};
        double result = 1;
        tbl[0] = x;
        for(int i=1;i<32;i++){
            tbl[i] = tbl[i-1]*tbl[i-1];
        }
        for(int i=0;i<32;i++){
            if( m & (0x1<<i) )
            result *= tbl[i];
        }
        return result;
    }
};