class Solution:
    def addDigits(self, num: int) -> int:
        # sum = 0
        # while num>=0:
        #     if 0<=sum<=9:
        #         break
        #     elif num==0:
        #         num=sum
        #         sum=0
        #     sum = sum+num%10
        #     num=num//10
        # return sum
        
        while num >= 10:
            sum = 0
            while num > 0:
                rem = num % 10 
                sum += rem
                num = num // 10
            num = sum
        return num