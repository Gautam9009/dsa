class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            a = haystack.index(needle)
            return a
        return -1