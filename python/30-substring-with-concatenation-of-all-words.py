# source: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def tokenize(s, start, step):
            tokens = []
            for i in range(start, len(s), step):
                tokens.append(s[i:i + step])
            print(tokens)
            return tokens
        
        results = []
        word_dict = collections.defaultdict(int)
        for word in words:
            word_dict[word] += 1
        n_word = len(words)
        if not words or not s:
            return results
        word_l = len(words[0])
        for i in range(word_l):
            k = i
            count = 0
            counter = collections.defaultdict(int)
            for j in range(i, len(s), word_l):
                token_j = s[j:j+word_l]
                if token_j in word_dict:
                    count += 1
                    counter[token_j] += 1
                    while k < j+word_l and counter[token_j] > word_dict[token_j]:
                        count -= 1
                        counter[s[k:k+word_l]] -= 1
                        k += word_l
                    if count == n_word:
                        results.append(k)
                else:
                    count = 0
                    counter.clear()
                    k = j+word_l
        
        return results
