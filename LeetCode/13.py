class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for idx in range(len(s)):
            if s[idx] == 'M':
                result+= 1000
            elif s[idx] == 'D':
                result+= 500
            elif s[idx] == 'C':
                if idx != len(s)-1 and (s[idx+1] == 'D' or s[idx+1] == 'M'):
                    result -= 100
                else:
                    result += 100
            elif s[idx] == 'L':
                result += 50
            elif s[idx] == 'X':
                if idx != len(s)-1 and (s[idx+1] == 'L' or s[idx+1] == 'C'):
                    result -= 10
                else:
                    result += 10
            elif s[idx] == 'V':
                result += 5
            else:
                if idx != len(s)-1 and (s[idx+1] == 'V' or s[idx+1] == 'X'):
                    result -= 1
                else:
                    result += 1
        return result
