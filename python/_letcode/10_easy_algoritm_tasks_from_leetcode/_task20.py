"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        opening = '({['
        closing = ')}]'
        direction = ''
        for char in s:
            if char in opening:
                direction += char
            if char in closing:
                if len(direction) == 0:
                    return False
                else:
                    if direction[-1] == opening[closing.index(char)]:
                        direction = direction[:-1]
                    else:
                        return False

        if len(direction) > 0:
            return False
        else:
            return True


s = Solution()
print(s.isValid('[({})]'))
print(s.isValid('[(){}[()]]'))
print(s.isValid('[(){}[(}]]'))