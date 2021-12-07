class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx_g = 0
        idx_s = 0
        cnt = 0
        while 1:
            if idx_g >= len(g) or idx_s >= len(s):
                break
            if g[idx_g] <= s[idx_s]:
                cnt += 1
                idx_g +=1
                idx_s +=1
            else:
                idx_s +=1
        return cnt
            
