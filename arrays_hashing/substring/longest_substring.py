class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        inicio = 0
        max_length = 0
        
        for index, char in enumerate(s):
            while char in seen:
                seen.remove(s[inicio])
                inicio += 1

            seen.add(char)
            max_length = max(max_length, (index-inicio)+1)
        
        return max_length
                