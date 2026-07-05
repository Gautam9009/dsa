class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        c = a[-1]
        d = len(c)
        return d
