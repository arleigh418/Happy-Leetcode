#Refer solution:no
#https://leetcode.com/problems/reverse-integer/
#Arleigh Chang
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''
class Solution(object):
    def reverse(self, x:int) -> int:
        if x < -2**31 or x > 2**31:
            return 0
        else:
            if x < 0 : 
                new_int = '-' 
                x = x*-1
            else : new_int = '' 
            str_x = str(x)
            for i in range(len(str_x)):
                new_int+=str_x[len(str_x)-i-1]
            result = int(new_int)    
            if result < -2**31 or result > 2**31:
                return 0
            else:
                return result

'''
Runtime: 36 ms, faster than 51.92% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.8 MB, less than 67.08% of Python3 online submissions for Reverse Integer.
'''