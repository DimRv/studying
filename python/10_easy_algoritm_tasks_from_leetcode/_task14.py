"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) > 1:
            pos = 0
            res = ''
            while pos < min([len(s) for s in strs]):
                char = strs[0][pos]
                for string in strs[1:]:
                    if string[pos] != char:
                        return res
                else:
                    res += char
                pos += 1
            return res
        else:
            return strs[0]


s = Solution()
print(s.longestCommonPrefix(["flower"]))
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))