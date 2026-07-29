class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(brackets[s[i]])
            elif len(stack) >= 1:
                if s[i] != stack.pop():
                    return False
            else:
                return False
        
        return stack == []

# Time: O(n)
# Space: O(n)
            