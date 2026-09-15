class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        target = s.split(" ")
        num=0
        for i in range(len(target)-1,-1,-1):
            if target[i]!="":
                num=len(target[i])
                break
        return num