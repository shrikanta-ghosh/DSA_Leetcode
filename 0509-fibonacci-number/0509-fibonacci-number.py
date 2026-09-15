class Solution:
    def fib(self, n: int) -> int:
        F = [0,1]
        for i in range(2,n+1):
            x=F[i-1]+F[i-2]
            F.append(x)
        return F[n]
        