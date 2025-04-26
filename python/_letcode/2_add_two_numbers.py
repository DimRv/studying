"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''
        for i in reversed(l1):
            num1 += str(i)
        for i in reversed(l2):
            num2 += str(i)
        res = int(num1) + int (num2)
        return [int(i) for i in reversed(str(res))]


print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(Solution().addTwoNumbers([0], [0]))
print(Solution().addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))
