class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = list(s)
        s.sort()
        s = list(set(s))
        s = ''.join(s)
        return s
        # Not Completed