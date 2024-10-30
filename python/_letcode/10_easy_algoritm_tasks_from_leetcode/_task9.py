"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if len(string) > 1:
            pos = 0
            while len(string) // 2 != pos:
                if string[pos] != string[-pos - 1]:
                    return False

                pos += 1
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(12321))
print(s.isPalindrome(123321))
print(s.isPalindrome(123421))
