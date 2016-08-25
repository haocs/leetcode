# source: https://leetcode.com/problems/scramble-string/

class Solution(object):
    def __init__(self):
        self.cache = {} # str -> bool
        
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        for a string AB, it's scramble string is BA
        """
        #print((s1, s2))
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1s2 = s1 + '&' + s2
        s2s1 = s2 + '&' + s1
        if s1s2 in self.cache:
            return self.cache[s1s2]
        if s2s1 in self.cache:
            return self.cache[s2s1]
        isScramble = False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                isScramble = True
                break
        self.cache[s1s2], self.cache[s2s1] = isScramble, isScramble
        return isScramble
