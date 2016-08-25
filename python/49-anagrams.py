# source: https://leetcode.com/problems/anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag_tracker = {} # str: list[str]
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anag_tracker:
                anag_tracker[sorted_s].append(s)
            else:
                anag_tracker[sorted_s] = [s]
        return [v for k, v in anag_tracker.items()]
