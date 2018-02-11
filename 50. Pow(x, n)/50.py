class Solution:
    myPow = pow


That’s even shorter than the other more obvious “cheat”:


class Solution:
    def myPow(self, x, n):
        return x ** n


And to calm down the haters, here’s me “doing it myself”:

Recursive:


class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


Iterative:


class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
