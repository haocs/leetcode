# source: https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = collections.defaultdict(int)
        for c in t:
            t_dict[c] += 1
        j = 0
        counter = collections.defaultdict(int)
        c_len = 0
        min_win = s + '####'
        for i in range(len(s)):
            cur = s[i]
            if cur in t_dict:
                counter[cur] += 1
                if counter[cur] <= t_dict[cur]:
                    c_len += 1
                while j <= i and (s[j] not in t_dict or counter[s[j]] > t_dict[s[j]]):
                    if s[j] in counter:
                        counter[s[j]] -= 1
                    j += 1
                if c_len == len(t) and len(min_win) > (i - j + 1):
                    min_win = s[j: i+1]
        if len(min_win) > len(s):
            return ''
        return min_win
                    
