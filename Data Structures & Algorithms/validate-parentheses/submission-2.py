class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(brackets[s[i]])
            elif len(stack) >= 1:
                close = stack.pop()
                if s[i] != close:
                    return False
            else:
                return False
        
        return stack == []
            