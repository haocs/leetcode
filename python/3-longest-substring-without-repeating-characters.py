# source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        n = len(s)
        length = 0
        min_start = 0
        l = 0
        counter = {}
        for r in range(n):
            char = s[r]
            while char in counter and counter[char] == 1:
                counter[s[l]] -= 1
                l += 1
            counter[char] = 1
            if r - l + 1 > length:
                length = r - l + 1
        return length
        
