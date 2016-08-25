# source: https://leetcode.com/problems/text-justification/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        def generate_line(words, max_w, words_w):
            if len(words) == 1:
                return words[0] + ' ' * (max_w - words_w)
            slot_num = len(words) - 1
            # pad for each slot includes: 1 space for each + base pad for each slot + extra pad which is 1 space and for first k left ones
            pad_w = max_w - words_w - slot_num
            base_w = 1 + pad_w / slot_num
            extra_pad_num = max_w - words_w - base_w * slot_num
            line = ''
            for i, word in enumerate(words):
                line += word + base_w * ' '
                if i < extra_pad_num:
                    line +=  ' '
            return line[:max_w]
        
        def generate_lastline(words, max_w, words_w):
            if not words:
                return ''
            line = ' '.join(words)
            line += ' ' * (max_w - len(line))
            return line
        
        lists = []
        while words:
            cur_w = 0
            cur = 0
            while cur < len(words) and cur_w + len(words[cur]) + cur <= maxWidth:
                cur_w += len(words[cur])
                cur += 1
            if cur == len(words):
                lists.append(generate_lastline(words, maxWidth, cur_w))
            else:
                lists.append(generate_line(words[:cur], maxWidth, cur_w))
            words = words[cur::]
        return lists   
