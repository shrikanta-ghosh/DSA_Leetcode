class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i
        num=num+1
        result=[]
        while num>0:
            result.append(num%10)
            num=num//10
        result=result[::-1]
        return result