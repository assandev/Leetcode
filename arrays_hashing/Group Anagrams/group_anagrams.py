from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for ch in w:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(w)
        return list(groups.values())