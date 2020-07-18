#Refer solution:no
#https://leetcode.com/problems/palindrome-number/
#Arleigh Chang
'''
Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution(object):
    def isPalindrome(self, x:int) -> bool:
        if x < 0 : return False
        elif x < 10 and x>=0 : return True
        elif x%10 ==0 : return False 
        else:
            x = str(x)
            target_len = len(x)
            for i in range(target_len):
                forward = i
                backward = len(x)-i-1
                if x[forward] == x[backward] : continue      
                else : return False         
            return True
'''
Runtime: 84 ms, faster than 33.30% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.7 MB, less than 89.50% of Python3 online submissions for Palindrome Number.
'''