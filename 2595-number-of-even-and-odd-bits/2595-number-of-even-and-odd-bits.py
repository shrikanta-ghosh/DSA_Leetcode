class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        n=bin(n)
        n=n[2:]
        n=n[::-1]
        for i,bit in enumerate(n):
            if bit=="1":
                if (i%2)!=0:
                    odd=odd+1
                else:
                    even+=1
        return [even, odd]
