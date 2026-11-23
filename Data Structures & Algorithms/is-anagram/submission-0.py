from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # This creates a frequency map automatically
        return Counter(s) == Counter(t)