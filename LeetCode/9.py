class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x)%2==0:
            n = len(x)//2-1
        else:
            n = len(x)//2
        if x[:len(x)//2] == x[:n:-1]:
            return True
        else:
            return False
